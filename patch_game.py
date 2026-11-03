# -*- coding: utf-8 -*-
"""
Freedom Fighters (IO Interactive - Glacier Engine)
Turkce Yama Kurucu ve Yonetici Scripti
Gelistirici: sqtbey
"""
import io, struct, zipfile, os, sys, json, argparse

COMMON_PATHS = [
    r'c:\Program Files\Epic Games\FreedomFighters',
    r'c:\Program Files (x86)\Steam\steamapps\common\Freedom Fighters',
    r'c:\Program Files\Steam\steamapps\common\Freedom Fighters',
    r'c:\GOG Games\Freedom Fighters',
    r'd:\Games\Freedom Fighters',
    r'e:\Games\Freedom Fighters',
]

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

def detect_game_dir(explicit_dir=None):
    if explicit_dir and os.path.exists(os.path.join(explicit_dir, 'Scenes')):
        return explicit_dir
    
    # Check current directory
    if os.path.exists('Scenes') and os.path.exists('Freedom.exe'):
        return os.path.abspath('.')
    
    # Check parent directory
    if os.path.exists('../Scenes') and os.path.exists('../Freedom.exe'):
        return os.path.abspath('..')
    
    # Check common paths
    for path in COMMON_PATHS:
        if os.path.exists(os.path.join(path, 'Scenes')):
            return path
            
    return None

def install_patch(game_dir, dict_path):
    scenes_dir = os.path.join(game_dir, 'Scenes')
    backup_dir = os.path.join(game_dir, 'Scenes_Backup')
    backup_zip_path = os.path.join(backup_dir, 'Original_LOC_Backup.zip')
    
    if not os.path.exists(dict_path):
        print(f"HATA: Ceviri sozlugu bulunamadi: {dict_path}")
        return False
        
    with open(dict_path, 'r', encoding='utf-8') as f:
        master_map = json.load(f)
    print(f"Yuklenen Turkce ceviriler: {len(master_map)} adet")
    
    os.makedirs(backup_dir, exist_ok=True)
    should_backup = not os.path.exists(backup_zip_path)
    
    targets = []
    for root, dirs, files in os.walk(scenes_dir):
        for f in files:
            if f.lower().endswith('.zip'):
                zpath = os.path.join(root, f)
                with zipfile.ZipFile(zpath, 'r') as zf:
                    for name in zf.namelist():
                        if name.lower().endswith('.loc'):
                            targets.append((zpath, name))
                            
    print(f"Yamalanacak dosya sayisi: {len(targets)} adet")
    
    total_trans = 0
    backup_mode = 'w' if should_backup else 'a'
    
    with zipfile.ZipFile(backup_zip_path, backup_mode, compression=zipfile.ZIP_DEFLATED) as backup_zip:
        for i, (zpath, loc_name) in enumerate(targets, 1):
            rel_name = os.path.relpath(zpath, scenes_dir)
            with zipfile.ZipFile(zpath, 'r') as zf:
                loc_raw = zf.read(loc_name)
                if should_backup:
                    key = rel_name.replace('\\', '/') + '::' + loc_name
                    backup_zip.writestr(key, loc_raw)
            
            tree = parse_loc_file(loc_raw)
            stats = {'translated': 0, 'untranslated': 0}
            translate_node(tree, master_map, stats)
            new_loc_raw = serialize_loc_file(tree)
            
            # Atomic ZIP update
            tmp_zip = zpath + '.tmp'
            with zipfile.ZipFile(zpath, 'r') as zf_in, \
                 zipfile.ZipFile(tmp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf_out:
                for item in zf_in.infolist():
                    if item.filename == loc_name:
                        zf_out.writestr(item, new_loc_raw)
                    else:
                        zf_out.writestr(item, zf_in.read(item.filename))
            os.replace(tmp_zip, zpath)
            total_trans += stats['translated']
            print(f"[{i:02d}/{len(targets):02d}] {rel_name} -> {stats['translated']} metin cevrildi.")
            
    print("\n" + "=" * 60)
    print("TEBRIKLER! Freedom Fighters Turkce Yama Basariyla Kuruldu!")
    print(f"Toplam uygulanan ceviri: {total_trans}")
    print(f"Yedek alinan dosya: {backup_zip_path}")
    print("=" * 60)
    return True

def uninstall_patch(game_dir):
    scenes_dir = os.path.join(game_dir, 'Scenes')
    backup_zip_path = os.path.join(game_dir, 'Scenes_Backup', 'Original_LOC_Backup.zip')
    
    if not os.path.exists(backup_zip_path):
        print(f"HATA: Orijinal yedek dosyasi bulunamadi: {backup_zip_path}")
        return False
        
    print("Orijinal dosyalar geri yukleniyor...")
    with zipfile.ZipFile(backup_zip_path, 'r') as bz:
        for item in bz.infolist():
            parts = item.filename.split('::')
            if len(parts) != 2:
                continue
            rel_zip, loc_name = parts
            zpath = os.path.join(scenes_dir, rel_zip.replace('/', os.sep))
            if not os.path.exists(zpath):
                continue
            orig_data = bz.read(item.filename)
            tmp_zip = zpath + '.tmp'
            with zipfile.ZipFile(zpath, 'r') as zf_in, \
                 zipfile.ZipFile(tmp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf_out:
                for zitem in zf_in.infolist():
                    if zitem.filename == loc_name:
                        zf_out.writestr(zitem, orig_data)
                    else:
                        zf_out.writestr(zitem, zf_in.read(zitem.filename))
            os.replace(tmp_zip, zpath)
            print(f"Geri yuklendi: {rel_zip}")
            
    print("\nOrijinal oyun dosyalari basariyla geri yuklendi!")
    return True

def main():
    parser = argparse.ArgumentParser(description="Freedom Fighters Turkce Yama Yoneticisi")
    parser.add_argument('--game-dir', type=str, help="Oyunun kurulu oldugu ana dizin")
    parser.add_argument('--uninstall', action='store_true', help="Yamayi kaldir ve orijinale don")
    args = parser.parse_args()
    
    print("=" * 60)
    print(" Freedom Fighters Turkce Yama v1.0")
    print(" Gelistirici: sqtbey")
    print("=" * 60)
    
    game_dir = detect_game_dir(args.game_dir)
    if not game_dir:
        print("Oyun dizini otomatik bulunamadi.")
        game_dir = input("Lutfen Freedom Fighters oyun klasorunu girin: ").strip('\"\' ')
        if not os.path.exists(os.path.join(game_dir, 'Scenes')):
            print("Gecersiz oyun dizini! 'Scenes' klasoru bulunamadi.")
            sys.exit(1)
            
    print(f"Hedef Oyun Dizini: {game_dir}")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dict_path = os.path.join(script_dir, 'master_translation_dict.json')
    
    if args.uninstall:
        uninstall_patch(game_dir)
    else:
        install_patch(game_dir, dict_path)

if __name__ == '__main__':
    main()
