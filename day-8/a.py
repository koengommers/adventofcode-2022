with open('input') as f:
    grid = []
    for line in f:
        grid.append([int(x) for x in line.strip()])

def get_column(i):
    return [x[i] for x in grid]

def get_row(i):
    return grid[i]

count = 0

for j in range(len(grid[0])):
    for i in range(len(grid)):
        height = grid[i][j]
        # check left
        if max(get_row(i)[:j] or [-1]) < height:
            count += 1
        # check right
        elif max(get_row(i)[j+1:] or [-1]) < height:
            count += 1
        # check top
        elif max(get_column(j)[:i] or [-1]) < height:
            count += 1
        # check bottom
        elif max(get_column(j)[i+1:] or [-1]) < height:
            count += 1

print(count)
