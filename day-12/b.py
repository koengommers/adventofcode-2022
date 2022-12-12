test = False

grid = []
letters = 'SabcdefghijklmnopqrstuvwxyzE'

with open('test' if test else 'input') as f:
    for y, line in enumerate(f):
        if 'S' in line:
            start = (line.index('S'), y)
        if 'E' in line:
            end = (line.index('E'), y)
        grid.append([list(letters).index(x) for x in line.strip()])

def get_neighbors(pos):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    possible = [(pos[0]+d[0], pos[1]+d[1]) for d in delta]
    return [p for p in possible if p[0] >= 0 and p[0] < len(grid[0]) and p[1] >= 0 and p[1] < len(grid)]

def get_height(pos):
    return grid[pos[1]][pos[0]]

distance_to_end = {
    end: 0
}

low_locations = []
for x in range(len(grid[0])):
    for y in range(len(grid)):
        if grid[y][x] == 1:
            low_locations.append((x, y))

while not any([l in distance_to_end for l in low_locations]):
    for pos in [k for k in distance_to_end.keys()]:
        height = get_height(pos)
        neighbors = get_neighbors(pos)
        for n in neighbors:
            if n not in distance_to_end and height - get_height(n) < 2:
                distance_to_end[n] = distance_to_end[pos] + 1

print(sorted([distance_to_end[l] for l in low_locations if l in distance_to_end])[0])
