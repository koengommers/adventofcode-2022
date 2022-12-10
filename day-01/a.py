with open('input') as f:
    elves = []
    current_elf = []
    for line in f:
        if line == '\n':
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(line))

elves_sum = [sum(elf) for elf in elves]
highest_sum = max(*elves_sum)
print(highest_sum)
