fully_contains = 0

def get_set_from_range(input):
    start, end = [int(x) for x in input.split('-')]
    return set(range(start, end+1))

with open('input') as f:
    for pair in f:
        first, second = [get_set_from_range(x) for x in pair.split(',')]
        if first.issubset(second) or second.issubset(first):
            fully_contains += 1

print(fully_contains)
