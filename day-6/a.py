MARKER_LENGTH = 4

def find_marker(input):
    for x in range(MARKER_LENGTH, len(input)):
        check = input[x-MARKER_LENGTH:x]
        if len(set(check)) == MARKER_LENGTH:
            return x

with open('input') as f:
    print(find_marker(f.readline()))
