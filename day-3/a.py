lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
letters = lowercase + uppercase

priority = 0

with open('input') as f:
    for rucksack in f:
        rucksack = list(rucksack.strip())
        first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        common = set(first).intersection(second).pop()
        priority += letters.index(common) + 1

print(priority)
