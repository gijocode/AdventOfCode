lines = [[int(y) for y in x.split()] for x in open("q9/inp.txt").read().splitlines()]


total = 0
for line in lines:
    row = line
    diff = 0
    while set(row) != {0}:
        diff += row[-1]
        row = list(map(lambda x: row[x + 1] - row[x], range(len(row) - 1)))

    total += diff

print("total", total)
