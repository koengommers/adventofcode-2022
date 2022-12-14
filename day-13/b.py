import functools

test = False

# should've probably used recursion but brain too fried
def make_list(input):
    buffer = ''
    buffers = []
    for char in input:
        if char == '[':
            buffers.append([])
        elif char == ']':
            if buffer:
                buffers[-1].append(int(buffer))
                buffer = ''
            if len(buffers) < 2:
                return buffers[0]
            else:
                buffers[-2].append(buffers.pop())
        elif char == ',':
            if buffer:
                buffers[-1].append(int(buffer))
                buffer = ''
        else:
            buffer += char

with open('test' if test else 'input') as f:
    packets = []
    for line in f:
        if line.strip() == '':
            pass
        else:
            packets.append(make_list(line.strip()))
    packets.append([[2]])
    packets.append([[6]])

def is_order_right(left, right):
    for i in range(max(len(left), len(right))):
        if i > len(left) - 1:
            return True
        elif i > len(right) - 1:
            return False
        elif type(left[i]) == list and type(right[i]) == list:
            check = is_order_right(left[i], right[i])
            if check is not None:
                return check
        elif type(left[i]) == list:
            check = is_order_right(left[i], [right[i]])
            if check is not None:
                return check
        elif type(right[i]) == list:
            check = is_order_right([left[i]], right[i])
            if check is not None:
                return check
        elif left[i] > right[i]:
            return False
        elif right[i] > left[i]:
            return True

def sort_by_order(a, b):
    return -1 if is_order_right(a, b) else 1

sorted_packets = sorted(packets, key=functools.cmp_to_key(sort_by_order))
print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
