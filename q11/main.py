lines_rows = [[y for y in x] for x in open("q11/inp.txt").read().splitlines()]

i = 0

while i < len(lines_rows):
    if not lines_rows[i].count("#"):
        lines_rows.insert(i, ["."] * len(lines_rows[0]))
        i += 1
    i += 1

i = 0
while i < len(lines_rows[0]):
    column = [x[i] for x in lines_rows]
    if not column.count("#"):
        x = 0
        while x < len(lines_rows):
            lines_rows[x].insert(i, ".")
            x += 1
        i += 1
    i += 1

galaxy_list = []
for x, line in enumerate(lines_rows):
    for y, char in enumerate(line):
        if char == "#":
            galaxy_list.append((x, y))

dist = 0
for i, galaxy in enumerate(galaxy_list):
    for dest_galaxy in galaxy_list[i:]:
        dist += abs(galaxy[0] - dest_galaxy[0]) + abs(galaxy[1] - dest_galaxy[1])
print(dist)
