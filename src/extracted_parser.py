python -c "
import io, struct, zipfile

with zipfile.ZipFile(r'Scenes\FF-StartUp.ZIP', 'r') as zf:
    orig_data = zf.read('SCENES/FF-StartUp.LOC')

class LocNode:
    def __init__(self, name='', value=None):
        self.name = name
        self.value = value # if leaf string
        self.children = []

def parse_tree(data_slice, name='', depth=0):
    stream = io.BytesIO(data_slice)
    node = LocNode(name)
    if len(data_slice) == 0:
        return node
    count = stream.read(1)[0]
    if count == 0:
        node.value = ''
        return node
    if count == 1:
        raw = bytearray()
        while True:
            b = stream.read(1)
            if not b or b == b'\x00':
                break
            raw.extend(b)
        first_str = raw.decode('utf-8', errors='replace')
        rem_len = len(data_slice) - stream.tell()
        if rem_len == 0:
            node.value = first_str
            return node
        else:
            child_data = data_slice[stream.tell():]
            child_node = parse_tree(child_data, name=first_str, depth=depth+1)
            node.children.append(child_node)
            return node
    else:
        offsets = []
        for _ in range(count - 1):
            offsets.append(struct.unpack('<I', stream.read(4))[0])
        first_child_pos = stream.tell()
        starts = [0] + offsets
        ends = offsets + [len(data_slice) - first_child_pos]
        for i in range(count):
            c_data = data_slice[first_child_pos + starts[i] : first_child_pos + ends[i]]
            c_stream = io.BytesIO(c_data)
            raw = bytearray()
            while True:
                b = c_stream.read(1)
                if not b or b == b'\x00':
                    break
                raw.extend(b)
            c_name = raw.decode('utf-8', errors='replace')
            c_body = c_data[c_stream.tell():]
            child_node = parse_tree(c_body, name=c_name, depth=depth+1)
            node.children.append(child_node)
        return node

# Serializer
def serialize_node_body(node):
    # Returns bytes of the node AFTER its name
    if node.value is not None:
        if node.value == '':
            return b'\x00'
        else:
            return b'\x01' + node.value.encode('utf-8') + b'\x00'
    elif len(node.children) == 1:
        # 1 child: count=1, then child name, then child body
        c = node.children[0]
        c_body = serialize_node_body(c)
        return b'\x01' + c.name.encode('utf-8') + b'\x00' + c_body
    else:
        count = len(node.children)
        c_serialized = []
        for c in node.children:
            c_bytes = c.name.encode('utf-8') + b'\x00' + serialize_node_body(c)
            c_serialized.append(c_bytes)
        # compute offsets
        offsets = []
        cur_off = 0
        for i in range(count - 1):
            cur_off += len(c_serialized[i])
            offsets.append(cur_off)
        header = bytes([count]) + b''.join(struct.pack('<I', off) for off in offsets)
        return header + b''.join(c_serialized)

# Parse original
stream = io.BytesIO(orig_data)
num_sec = stream.read(1)[0]
sec_offsets = [struct.unpack('<I', stream.read(4))[0] for _ in range(num_sec - 1)]
first_sec_pos = 1 + 4 * (num_sec - 1)
starts = [0] + sec_offsets
ends = sec_offsets + [len(orig_data) - first_sec_pos]

root_sections = []
for i in range(num_sec):
    sec_data = orig_data[first_sec_pos + starts[i] : first_sec_pos + ends[i]]
    s_stream = io.BytesIO(sec_data)
    raw = bytearray()
    while True:
        b = s_stream.read(1)
        if not b or b == b'\x00':
            break
        raw.extend(b)
    s_name = raw.decode('utf-8', errors='replace')
    s_body = sec_data[s_stream.tell():]
    sec_node = parse_tree(s_body, name=s_name, depth=1)
    root_sections.append(sec_node)

# Serialize root
root_node = LocNode()
root_node.children = root_sections
count = len(root_node.children)
c_serialized = []
for c in root_node.children:
    c_bytes = c.name.encode('utf-8') + b'\x00' + serialize_node_body(c)
    c_serialized.append(c_bytes)
offsets = []
cur_off = 0
for i in range(count - 1):
    cur_off += len(c_serialized[i])
    offsets.append(cur_off)
new_data = bytes([count]) + b''.join(struct.pack('<I', off) for off in offsets) + b''.join(c_serialized)

print(f'Original size: {len(orig_data)}, Serialized size: {len(new_data)}')
print(f'Byte-for-byte identical? {orig_data == new_data}')
if orig_data != new_data:
    for i in range(min(len(orig_data), len(new_data))):
        if orig_data[i] != new_data[i]:
            print(f'First diff at {i}: orig={orig_data[i]:#x}, new={new_data[i]:#x}')
            print('Orig:', orig_data[max(0, i-20):i+20])
            print('New: ', new_data[max(0, i-20):i+20])
            break
"