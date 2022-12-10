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
rope_length = 9
rope = [(0, 0)]*rope_length
head = (0, 0)

visited.add(rope[-1])

for x, y in steps:
    head = (head[0] + x, head[1] + y)
    rope_before = head

    for i in range(len(rope)):
        # rope before is still within one position of tail
        if abs(rope_before[0] - rope[i][0]) <= 1 and abs(rope_before[1] - rope[i][1]) <= 1:
            pass
        elif rope_before[0] == rope[i][0]:
            if rope[i][1] > rope_before[1]:
                rope[i] = (rope[i][0], rope[i][1] - 1)
            elif rope[i][1] < rope_before[1]:
                rope[i] = (rope[i][0], rope[i][1] + 1)
        elif rope_before[1] == rope[i][1]:
            if rope[i][0] > rope_before[0]:
                rope[i] = (rope[i][0] - 1, rope[i][1])
            elif rope[i][0] < rope_before[0]:
                rope[i] = (rope[i][0] + 1, rope[i][1])
        else:
            if rope[i][1] > rope_before[1]:
                rope[i] = (rope[i][0], rope[i][1] - 1)
            elif rope[i][1] < rope_before[1]:
                rope[i] = (rope[i][0], rope[i][1] + 1)

            if rope[i][0] > rope_before[0]:
                rope[i] = (rope[i][0] - 1, rope[i][1])
            elif rope[i][0] < rope_before[0]:
                rope[i] = (rope[i][0] + 1, rope[i][1])

        rope_before = rope[i]

    visited.add(rope[-1])

print(len(visited))
