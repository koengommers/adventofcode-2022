from functools import reduce

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
letters = lowercase + uppercase

priority = 0

with open('input') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        rucksacks = [set(list(line.strip())) for line in lines[i:i+3]]
        common = reduce(lambda a, b: a & b, rucksacks).pop()
        priority += letters.index(common) + 1

print(priority)
