with open('input') as f:
    grid = []
    for line in f:
        grid.append([int(x) for x in line.strip()])

def get_column(i):
    return [x[i] for x in grid]

def get_row(i):
    return grid[i]

def check_distance(trees, height):
    # is at the edge
    if not trees:
        return 0

    for i, tree in enumerate(trees, 1):
        if tree >= height:
            return i

    # can see all the way to the edge
    return len(trees)

highscore = 0

for j in range(len(grid[0])):
    for i in range(len(grid)):
        height = grid[i][j]
        # check left
        left = check_distance(get_row(i)[:j][::-1], height)
        # check right
        right = check_distance(get_row(i)[j+1:], height)
        # check top
        up = check_distance(get_column(j)[:i][::-1], height)
        # check bottom
        down = check_distance(get_column(j)[i+1:], height)

        score = left * right * up * down
        highscore = max(highscore, score)

print(highscore)
