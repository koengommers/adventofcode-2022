signal_changes = [1]

with open('input') as f:
    for line in f:
        signal_changes.append(0)
        if line.startswith('addx'):
            signal_changes.append(int(line.strip().split()[-1]))

total = 0
cycles = [20, 60, 100, 140, 180, 220]
for cycle in cycles:
    total += cycle * sum(signal_changes[:cycle])

print(total)
