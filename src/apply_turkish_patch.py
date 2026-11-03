# -*- coding: utf-8 -*-
"""
Freedom Fighters Turkish Patch Application Script.
Backs up original .LOC files and patches all 88 .LOC files inside Scenes/*.ZIP.
"""
import io, struct, zipfile, os, sys, shutil, json, tempfile

WORKSPACE = r'c:\Program Files\Epic Games\FreedomFighters'
SCENES_DIR = os.path.join(WORKSPACE, 'Scenes')
BACKUP_DIR = os.path.join(WORKSPACE, 'Scenes_Backup')
MASTER_DICT_PATH = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline\master_translation_dict.json'

class LocNode:
    def __init__(self, name=''):
        self.name = name
        self.strings = []
        self.children = []
        self.trailing = b''
        self.is_leaf = False
        self.string_count_byte = 1

def read_cstring(stream):
    raw = bytearray()
    while True:
        b = stream.read(1)
        if not b or b == b'\x00':
            break
        raw.extend(b)
    return raw.decode('utf-8', errors='replace')

def parse_chunk(data_slice, name=''):
    node = LocNode(name)
    if len(data_slice) == 0:
        node.is_leaf = True
        return node
    
    stream = io.BytesIO(data_slice)
    count = stream.read(1)[0]
    
    if count == 0:
        node.is_leaf = True
        node.strings = ['']
        node.trailing = stream.read()
        return node
    
    if count == 1:
        first_str = read_cstring(stream)
        rem = data_slice[stream.tell():]
        if len(rem) == 0 or rem.strip(b'\r\n\x00') == b'':
            node.is_leaf = True
            node.strings = [first_str]
            node.trailing = rem
            return node
        else:
            child_node = parse_chunk(rem, name=first_str)
            node.children.append(child_node)
            return node
    else:
        has_offsets = False
        needed_bytes = 4 * (count - 1)
        rem_len = len(data_slice) - 1
        if rem_len >= needed_bytes:
            offsets = []
            cur_pos = stream.tell()
            for _ in range(count - 1):
                off = struct.unpack('<I', stream.read(4))[0]
                offsets.append(off)
            stream.seek(cur_pos)
            max_child_space = rem_len - needed_bytes
            if all(0 < offsets[i] for i in range(len(offsets))) and \
               all(offsets[i] < offsets[i+1] for i in range(len(offsets)-1)) and \
               offsets[-1] < max_child_space:
                has_offsets = True
        
        if has_offsets:
            offsets = [struct.unpack('<I', stream.read(4))[0] for _ in range(count - 1)]
            child_base = stream.tell()
            starts = [0] + offsets
            ends = offsets + [len(data_slice) - child_base]
            for i in range(count):
                c_data = data_slice[child_base + starts[i] : child_base + ends[i]]
                c_stream = io.BytesIO(c_data)
                c_name = read_cstring(c_stream)
                c_body = c_data[c_stream.tell():]
                c_node = parse_chunk(c_body, name=c_name)
                node.children.append(c_node)
            return node
        else:
            node.is_leaf = True
            strings = []
            while stream.tell() < len(data_slice):
                s = read_cstring(stream)
                strings.append(s)
                if stream.tell() == len(data_slice):
                    break
                rem = data_slice[stream.tell():]
                if rem.strip(b'\r\n\x00') == b'':
                    node.trailing = rem
                    break
            node.strings = strings
            node.string_count_byte = count
            return node

def parse_loc_file(loc_bytes):
    stream = io.BytesIO(loc_bytes)
    num_sec = stream.read(1)[0]
    sec_offsets = [struct.unpack('<I', stream.read(4))[0] for _ in range(num_sec - 1)]
    first_sec_pos = 1 + 4 * (num_sec - 1)
    starts = [0] + sec_offsets
    ends = sec_offsets + [len(loc_bytes) - first_sec_pos]

    root = LocNode()
    for i in range(num_sec):
        sec_data = loc_bytes[first_sec_pos + starts[i] : first_sec_pos + ends[i]]
        s_stream = io.BytesIO(sec_data)
        s_name = read_cstring(s_stream)
        s_body = sec_data[s_stream.tell():]
        sec_node = parse_chunk(s_body, name=s_name)
        root.children.append(sec_node)
    return root

def serialize_chunk(node):
    if node.is_leaf:
        if not node.strings or (len(node.strings) == 1 and node.strings[0] == '' and not node.trailing):
            return b'\x00' + node.trailing
        if len(node.strings) == 1 and node.string_count_byte == 1:
            return b'\x01' + node.strings[0].encode('utf-8') + b'\x00' + node.trailing
        else:
            count = getattr(node, 'string_count_byte', len(node.strings))
            out = bytes([count])
            for s in node.strings:
                out += s.encode('utf-8') + b'\x00'
            return out + node.trailing
    elif len(node.children) == 1:
        c = node.children[0]
        c_body = serialize_chunk(c)
        return b'\x01' + c.name.encode('utf-8') + b'\x00' + c_body
    else:
        count = len(node.children)
        c_serialized = []
        for c in node.children:
            c_bytes = c.name.encode('utf-8') + b'\x00' + serialize_chunk(c)
            c_serialized.append(c_bytes)
        offsets = []
        cur_off = 0
        for i in range(count - 1):
            cur_off += len(c_serialized[i])
            offsets.append(cur_off)
        header = bytes([count]) + b''.join(struct.pack('<I', off) for off in offsets)
        return header + b''.join(c_serialized)

def serialize_loc_file(root):
    count = len(root.children)
    c_serialized = []
    for c in root.children:
        c_bytes = c.name.encode('utf-8') + b'\x00' + serialize_chunk(c)
        c_serialized.append(c_bytes)
    offsets = []
    cur_off = 0
    for i in range(count - 1):
        cur_off += len(c_serialized[i])
        offsets.append(cur_off)
    header = bytes([count]) + b''.join(struct.pack('<I', off) for off in offsets)
    return header + b''.join(c_serialized)

def translate_node(node, translations, stats):
    if node.is_leaf:
        new_strings = []
        for s in node.strings:
            if not s.strip():
                new_strings.append(s)
                continue
            if s in translations:
                new_strings.append(translations[s])
                stats['translated'] += 1
            elif s.strip() in translations:
                prefix = s[:len(s) - len(s.lstrip())]
                suffix = s[len(s.rstrip()):]
                new_strings.append(prefix + translations[s.strip()] + suffix)
                stats['translated'] += 1
            else:
                new_strings.append(s)
                stats['untranslated'] += 1
        node.strings = new_strings
    else:
        for c in node.children:
            translate_node(c, translations, stats)

def patch_zip_file(zip_path, loc_filename, master_map, backup_zip):
    # 1. Read original loc
    with zipfile.ZipFile(zip_path, 'r') as zf:
        orig_loc_data = zf.read(loc_filename)
        rel_zip_path = os.path.relpath(zip_path, SCENES_DIR)
        backup_zip_loc_name = rel_zip_path.replace('\\', '/') + '::' + loc_filename
        backup_zip.writestr(backup_zip_loc_name, orig_loc_data)

    # 2. Parse and translate
    tree = parse_loc_file(orig_loc_data)
    stats = {'translated': 0, 'untranslated': 0}
    translate_node(tree, master_map, stats)
    new_loc_data = serialize_loc_file(tree)

    # Verify new loc roundtrip integrity
    verify_tree = parse_loc_file(new_loc_data)
    if new_loc_data != serialize_loc_file(verify_tree):
        raise ValueError(f"Integrity check failed for {loc_filename}")

    # 3. Update ZIP archive safely
    temp_zip = zip_path + '.tmp'
    with zipfile.ZipFile(zip_path, 'r') as zf_in, \
         zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf_out:
        for item in zf_in.infolist():
            if item.filename == loc_filename:
                # Write patched data
                zf_out.writestr(item, new_loc_data)
            else:
                zf_out.writestr(item, zf_in.read(item.filename))

    # Replace original zip with patched zip
    os.replace(temp_zip, zip_path)
    return stats

def main():
    print("=" * 60)
    print("Freedom Fighters Turkce Yama Kurulumu")
    print("=" * 60)

    with open(MASTER_DICT_PATH, 'r', encoding='utf-8') as f:
        master_map = json.load(f)
    print(f"Yuklenen Turkce ceviriler: {len(master_map)} adet")

    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup_zip_path = os.path.join(BACKUP_DIR, 'Original_LOC_Backup.zip')
    print(f"Yedek dosyasi olusturuluyor: {backup_zip_path}")

    # Find all ZIPs with LOC
    targets = []
    for root, dirs, files in os.walk(SCENES_DIR):
        for f in files:
            if f.lower().endswith('.zip'):
                zpath = os.path.join(root, f)
                with zipfile.ZipFile(zpath, 'r') as zf:
                    for name in zf.namelist():
                        if name.lower().endswith('.loc'):
                            targets.append((zpath, name))

    print(f"Yamalanacak .LOC dosyalari: {len(targets)} adet")

    total_translated = 0
    total_untranslated = 0

    with zipfile.ZipFile(backup_zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as backup_zip:
        for i, (zpath, loc_name) in enumerate(targets, 1):
            rel_name = os.path.relpath(zpath, SCENES_DIR)
            stats = patch_zip_file(zpath, loc_name, master_map, backup_zip)
            total_translated += stats['translated']
            total_untranslated += stats['untranslated']
            print(f"[{i:02d}/{len(targets):02d}] {rel_name} ({loc_name}) -> Cevrilen: {stats['translated']}")

    print("\n" + "=" * 60)
    print(f"Yama Basariyla Tamamlandi!")
    print(f"Toplam ceviri uygulanan metin: {total_translated}")
    print(f"Cevrilmeyen (Krediler / font test): {total_untranslated}")
    print(f"Orijinal yedek kaydedildi: {backup_zip_path}")
    print("=" * 60)

if __name__ == '__main__':
    main()
