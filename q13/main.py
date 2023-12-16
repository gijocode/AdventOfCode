def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        above = above[: len(below)]
        below = below[: len(above)]
        if above == below:
            return r
    return 0


patterns_horizontal = [x.split() for x in open("q13/inp.txt").read().split("\n\n")]

total_row = 0
total_column = 0

for pattern in patterns_horizontal:
    total_row += find_mirror(pattern) * 100
    total_column += find_mirror(list(zip(*pattern)))
print(total_row + total_column)
