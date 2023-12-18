from copy import deepcopy

grid = [[y for y in x.strip()] for x in open("q14/inp.txt").readlines()]


def rotate(grid):
    for _ in range(4):
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] == "O":
                    for x in range(i - 1, -1, -1):
                        if grid[x][j] != ".":
                            break
                        grid[x][j] = "O"
                        grid[x + 1][j] = "."
        grid = [list(x) for x in zip(*reversed(grid))]
    return grid


grid_list = []
while True:
    grid_list.append(deepcopy(grid))
    grid = rotate(grid)
    if grid in grid_list:
        cycle_start = grid_list.index(grid)
        cycle_length = len(grid_list) - cycle_start
        break

remaining_rots = (1_000_000_000 - cycle_start) % (cycle_length)


for _ in range(remaining_rots):
    grid = rotate(grid)

total = 0
for i, x in enumerate(grid[::-1]):
    total += (i + 1) * x.count("O")
print(total)
