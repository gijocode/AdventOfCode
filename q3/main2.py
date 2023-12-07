lines = []
with open("q3/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        lines.append(line.strip())
line = line.strip()


def getNo(x, y):
    start = 0
    for i in range(y, -1, -1):
        if not lines[x][i].isdigit():
            start = i + 1
            break
    num = 0
    for j in range(start, len(line)):
        if not lines[x][j].isdigit():
            return num
        num = (num * 10) + int(lines[x][j])
    return num


def isGear(x, y):
    surround_nos = set()
    if x >= 1:
        if y >= 1 and lines[x - 1][y - 1].isdigit():
            surround_nos.add(getNo(x - 1, y - 1))
        if lines[x - 1][y].isdigit():
            surround_nos.add(getNo(x - 1, y))
        if y < len(line) - 1 and lines[x - 1][y + 1].isdigit():
            surround_nos.add(getNo(x - 1, y + 1))
    if x < len(lines) - 1:
        if y >= 1 and lines[x + 1][y - 1].isdigit():
            surround_nos.add(getNo(x + 1, y - 1))
        if lines[x + 1][y].isdigit():
            surround_nos.add(getNo(x + 1, y))
        if y < len(line) - 1 and lines[x + 1][y + 1].isdigit():
            surround_nos.add(getNo(x + 1, y + 1))
    if y >= 1 and lines[x][y - 1].isdigit():
        surround_nos.add(getNo(x, y - 1))
    if y <= len(line) and lines[x][y + 1].isdigit():
        surround_nos.add(getNo(x, y + 1))

    surround_nos = list(surround_nos)
    if len(surround_nos) == 2:
        product = 1
        for n in surround_nos:
            product = product * n
        return product
    return 0


total = 0
for i in range(len(lines)):
    for j in range(len(line)):
        if lines[i][j] == "*":
            total += isGear(i, j)

print(total)
