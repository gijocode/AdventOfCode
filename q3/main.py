lines = []
with open("q3/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        lines.append(line.strip())


def isEnginePart(row, column, offset):
    coords = []
    if row > 0:
        if column > 0:
            coords.append(lines[row - 1][column - 1])
        if column + offset < len(line) - 1:
            coords.append(lines[row - 1][column + offset])
        for i in range(offset):
            coords.append(lines[row - 1][column + i])
    if row < len(lines) - 1:
        if column > 0:
            coords.append(lines[row + 1][column - 1])
        if column + offset < len(line) - 1:
            coords.append(lines[row + 1][column + offset])
        for i in range(offset):
            coords.append(lines[row + 1][column + i])
    if column + offset < len(line) - 1:
        coords.append(lines[row][column + offset])
    if column > 0:
        coords.append(lines[row][column - 1])
    print(coords)

    for ch in coords:
        if not ch.isdigit() and ch != ".":
            return True
    return False


def get_current_no(row, column):
    num = 0
    for i in range(column, len(lines[0])):
        if not lines[row][i].isdigit():
            break
        num = (num * 10) + int(lines[row][i])
    return num, i - column


print(lines)
total = 0
for i in range(len(lines)):
    j = 0
    while j in range(len(line) - 1):
        if n := lines[i][j].isdigit():
            current_no, offset = get_current_no(i, j)
            print(lines[i])
            print(current_no)
            if isEnginePart(i, j, offset):
                total += current_no
            j = j + offset + 1
        else:
            j = j + 1
print(total)
