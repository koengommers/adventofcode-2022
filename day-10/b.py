signal_changes = [1]

with open('input') as f:
    for line in f:
        signal_changes.append(0)
        if line.startswith('addx'):
            signal_changes.append(int(line.strip().split()[-1]))

screen = []
for i in range(6):
    row = ''
    for j in range(40):
        cycle = i * 40 + j + 1
        position = sum(signal_changes[:cycle])
        if abs(((cycle - 1) % 40) - position) <= 1:
            row += '#'
        else:
            row += '.'
    screen.append(row)

for row in screen:
    print(row)
