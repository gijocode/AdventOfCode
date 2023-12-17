from pprint import pprint

grid = [[y for y in x.strip()] for x in open("q14/inp2.txt").readlines()]

for j in range(len(grid[0])):
    for i in range(1, len(grid)):
        if grid[i][j] == "O":
            for x in range(i - 1, -1, -1):
                if grid[x][j] != ".":
                    break
                grid[x][j] = "O"
                grid[x + 1][j] = "."
total = 0
for i, x in enumerate(grid[::-1]):
    total += (i + 1) * x.count("O")
print(total)

pprint(grid)

pprint([list(x) for x in zip(*reversed(grid))])
