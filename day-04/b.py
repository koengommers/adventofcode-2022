overlaps = 0

def get_set_from_range(input):
    start, end = [int(x) for x in input.split('-')]
    return set(range(start, end+1))

with open('input') as f:
    for pair in f:
        first, second = [get_set_from_range(x) for x in pair.split(',')]
        if not first.isdisjoint(second):
            overlaps += 1

print(overlaps)
