import time

st = time.perf_counter()
lines_rows = [
    [[y, [i, j]] for j, y in enumerate(x)]
    for i, x in enumerate(open("q11/inp.txt").read().splitlines())
]

height = len(lines_rows)
width = len(lines_rows[0])

i = 0
while i < height:
    if not [x[0] for x in lines_rows[i]].count("#"):
        for x in range(i, height):
            for y in range(width):
                lines_rows[x][y][1][0] += 999_999
    i += 1

i = 0
while i < width:
    column = [x[i][0] for x in lines_rows]
    if not column.count("#"):
        for x in range(i, width):
            for y in range(height):
                lines_rows[y][x][1][1] += 999_999
    i += 1
galaxy_list = []
for x, line in enumerate(lines_rows):
    for y, char in enumerate(line):
        if char[0] == "#":
            galaxy_list.append(char[1])

dist = 0
for i, galaxy in enumerate(galaxy_list):
    for dest_galaxy in galaxy_list[i + 1 :]:
        dist += abs(galaxy[0] - dest_galaxy[0]) + abs(galaxy[1] - dest_galaxy[1])
print(dist)

print(f"took {(time.perf_counter() - st)*1000:0.4f}ms")
