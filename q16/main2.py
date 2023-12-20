import sys

sys.setrecursionlimit(9999)

grid = [[x for x in y.strip()] for y in open("q16/inp.txt").readlines()]
height, width = len(grid), len(grid[0])


def do_work(start, direction):
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

    seen = []
    travel(start, direction)
    path = {x[0] for x in seen}
    return len(path) - 1


d = [do_work((height, i), "up") for i in range(width)]
u = [do_work((-1, i), "down") for i in range(width)]
r = [do_work((i, -1), "right") for i in range(height)]
l = [do_work((i, width), "left") for i in range(height)]
print("max", max(r + l + u + d))
