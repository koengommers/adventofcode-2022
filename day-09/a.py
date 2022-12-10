directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

with open('input') as f:
    input = [line.strip().split() for line in f]
    motions = [(x[0], int(x[1])) for x in input]
    steps = []
    for direction, n in motions:
        steps += [directions[direction]] * n

visited = set()
head = (0, 0)
tail = (0, 0)

visited.add(tail)

for x, y in steps:
    head = (head[0] + x, head[1] + y)

    # head is still within one position of tail
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        continue

    if head[0] == tail[0]:
        if tail[1] > head[1]:
            tail = (tail[0], tail[1] - 1)
        elif tail[1] < head[1]:
            tail = (tail[0], tail[1] + 1)
    elif head[1] == tail[1]:
        if tail[0] > head[0]:
            tail = (tail[0] - 1, tail[1])
        elif tail[0] < head[0]:
            tail = (tail[0] + 1, tail[1])
    else:
        if tail[1] > head[1]:
            tail = (tail[0], tail[1] - 1)
        elif tail[1] < head[1]:
            tail = (tail[0], tail[1] + 1)

        if tail[0] > head[0]:
            tail = (tail[0] - 1, tail[1])
        elif tail[0] < head[0]:
            tail = (tail[0] + 1, tail[1])

    visited.add(tail)

print(len(visited))
