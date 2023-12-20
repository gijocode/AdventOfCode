grid = [[x for x in y.strip()] for y in open("q16/inp.txt").readlines()]

start = (0, -1)
height, width = len(grid), len(grid[0])
seen = []
import sys

sys.setrecursionlimit(9999)


def travel(coords, direction):
    if (coords, direction) in seen:
        return
    seen.append((coords, direction))
    if direction == "right":
        coords = (coords[0], coords[1] + 1)
        if coords[1] >= width:
            return
        if grid[coords[0]][coords[1]] in [".", "-"]:
            return travel(coords, direction)
        elif grid[coords[0]][coords[1]] == "|":
            return travel(coords, "up"), travel(coords, "down")
        elif grid[coords[0]][coords[1]] == "\\":
            return travel(coords, "down")
        elif grid[coords[0]][coords[1]] == "/":
            return travel(coords, "up")

    elif direction == "left":
        coords = (coords[0], coords[1] - 1)
        if coords[1] < 0:
            return
        if grid[coords[0]][coords[1]] in [".", "-"]:
            return travel(coords, direction)
        elif grid[coords[0]][coords[1]] == "|":
            return travel(coords, "up"), travel(coords, "down")
        elif grid[coords[0]][coords[1]] == "\\":
            return travel(coords, "up")
        elif grid[coords[0]][coords[1]] == "/":
            return travel(coords, "down")

    elif direction == "up":
        coords = (coords[0] - 1, coords[1])
        if coords[0] < 0:
            return
        if grid[coords[0]][coords[1]] in [".", "|"]:
            return travel(coords, direction)
        elif grid[coords[0]][coords[1]] == "-":
            return travel(coords, "left"), travel(coords, "right")
        elif grid[coords[0]][coords[1]] == "\\":
            return travel(coords, "left")
        elif grid[coords[0]][coords[1]] == "/":
            return travel(coords, "right")

    elif direction == "down":
        coords = (coords[0] + 1, coords[1])
        if coords[0] >= height:
            return
        if grid[coords[0]][coords[1]] in [".", "|"]:
            return travel(coords, direction)
        elif grid[coords[0]][coords[1]] == "-":
            return travel(coords, "left"), travel(coords, "right")
        elif grid[coords[0]][coords[1]] == "\\":
            return travel(coords, "right")
        elif grid[coords[0]][coords[1]] == "/":
            return travel(coords, "left")


travel(start, "right")

path = {x[0] for x in seen}
print(len(path) - 1)
