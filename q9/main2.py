lines = [[int(y) for y in x.split()] for x in open("q9/inp.txt").read().splitlines()]


final = 0
for line in lines:
    total = 0
    row = line
    diff = []
    while set(row) != {0}:
        diff.append(row[0])
        row = list(map(lambda x: row[x + 1] - row[x], range(len(row) - 1)))

    for x in diff[::-1]:
        total = x - total
    final += total

print("total", final)
