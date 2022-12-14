test = False

cave = dict()

with open('test' if test else 'input') as f:
    for line in f:
        points = line.strip().split(' -> ')
        coordinates = [tuple([int(x) for x in point.split(',')]) for point in points]
        for i in range(len(coordinates) - 1):
            coords = coordinates[i]
            next_coords = coordinates[i+1]
            for x in range(coords[0], next_coords[0], 1 if next_coords[0] > coords[0] else -1):
                cave[(x, coords[1])] = '#'
            for y in range(coords[1], next_coords[1], 1 if next_coords[1] > coords[1] else -1):
                cave[(coords[0], y)] = '#'
            cave[next_coords] = '#'

def print_cave():
    min_x = min([x for x, _ in cave.keys()])
    max_x = max([x for x, _ in cave.keys()])
    min_y = 0
    max_y = max([y for _, y in cave.keys()])
    for y in range(min_y, max_y+1):
        print(''.join([cave[(x,y)] if (x,y) in cave else '.' for x in range(min_x, max_x+1)]))

print_cave()
lowest_point_in_cave = max([y for _, y in cave.keys()])

sand = (500, 0)

while sand[1] < lowest_point_in_cave:
    if (sand[0], sand[1]+1) not in cave:
        sand = sand[0], sand[1]+1
    elif (sand[0]-1, sand[1]+1) not in cave:
        sand = sand[0]-1, sand[1]+1
    elif (sand[0]+1, sand[1]+1) not in cave:
        sand = sand[0]+1, sand[1]+1
    else:
        cave[sand] = 'o'
        print_cave()
        sand = (500, 0)

print(len([x for x in cave.values() if x == 'o']))
