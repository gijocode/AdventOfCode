from copy import deepcopy


def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[: len(below)]
        below = below[: len(above)]
        for i, (x, y) in enumerate(zip(above, below)):
            for j, (a, b) in enumerate(zip(x, y)):
                if a != b:
                    changed = deepcopy(above)
                    changed[i][j] = "." if above[i][j] == "#" else "#"
                    if changed == below:
                        return r
                    break
    return 0


patterns_horizontal = [x.split() for x in open("q13/inp.txt").read().split("\n\n")]
converted_patterns = [[list(r) for r in pattern] for pattern in patterns_horizontal]

total_row = 0
total_column = 0

for pattern in converted_patterns:
    total_row += find_mirror(pattern) * 100
    l = []
    for x in list(zip(*pattern)):
        if type(x) == tuple:
            l.append(list(x))
        else:
            l.append(x)
    total_column += find_mirror(l)
print(total_row + total_column)
