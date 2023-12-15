lines = [[y for y in x] for x in open("q10/inp.txt").read().splitlines()]

height = len(lines)
width = len(lines[0])
for i, line in enumerate(lines):
    if "S" in line:
        start_coords = (i, line.index("S"))
        break

for x in range(4):
    walk = 0
    walked_coords = []
    prev = lines[start_coords[0]][start_coords[1]]
    if x == 0:
        current_coords = (start_coords[0] - 1, start_coords[1])
    elif x == 1:
        current_coords = (start_coords[0] + 1, start_coords[1])
    elif x == 2:
        current_coords = (start_coords[0], start_coords[1] - 1)
    elif x == 3:
        current_coords = (start_coords[0], start_coords[1] + 1)
    # first_joint_coords = current_coords
    walked_coords.append(start_coords)
    walked_coords.append(current_coords)
    current = lines[current_coords[0]][current_coords[1]]
    walk += 1
    while True:
        if current == "|":
            if (
                current_coords[0] - 1 >= 0
                and (current_coords[0] - 1, current_coords[1]) not in walked_coords
            ):
                current_coords = (current_coords[0] - 1, current_coords[1])
            elif (
                current_coords[0] + 1 < height
                and (current_coords[0] + 1, current_coords[1]) not in walked_coords
            ):
                current_coords = (current_coords[0] + 1, current_coords[1])
            else:
                walk = 0
                break
        elif current == "-":
            if (
                current_coords[1] - 1 >= 0
                and (current_coords[0], current_coords[1] - 1) not in walked_coords
            ):
                current_coords = (current_coords[0], current_coords[1] - 1)
            elif (
                current_coords[1] + 1 < width
                and (current_coords[0], current_coords[1] + 1) not in walked_coords
            ):
                current_coords = (current_coords[0], current_coords[1] + 1)
            else:
                walk = 0
                break
        elif current == "L":
            if (
                current_coords[0] - 1 >= 0
                and (current_coords[0] - 1, current_coords[1]) not in walked_coords
            ):
                current_coords = (current_coords[0] - 1, current_coords[1])
            elif (
                current_coords[1] + 1 < width
                and (current_coords[0], current_coords[1] + 1) not in walked_coords
            ):
                current_coords = (current_coords[0], current_coords[1] + 1)
            else:
                walk = 0
                break
        elif current == "J":
            if (
                current_coords[0] - 1 >= 0
                and (current_coords[0] - 1, current_coords[1]) not in walked_coords
            ):
                current_coords = (current_coords[0] - 1, current_coords[1])
            elif (
                current_coords[1] - 1 >= 0
                and (current_coords[0], current_coords[1] - 1) not in walked_coords
            ):
                current_coords = (current_coords[0], current_coords[1] - 1)
            else:
                walk = 0
                break
        elif current == "7":
            if (
                current_coords[0] + 1 < height
                and (current_coords[0] + 1, current_coords[1]) not in walked_coords
            ):
                current_coords = (current_coords[0] + 1, current_coords[1])
            elif (
                current_coords[1] - 1 >= 0
                and (current_coords[0], current_coords[1] - 1) not in walked_coords
            ):
                current_coords = (current_coords[0], current_coords[1] - 1)
            else:
                walk = 0
                break

        elif current == "F":
            if (
                current_coords[0] + 1 < height
                and (current_coords[0] + 1, current_coords[1]) not in walked_coords
            ):
                current_coords = (current_coords[0] + 1, current_coords[1])
            elif (
                current_coords[1] + 1 < width
                and (current_coords[0], current_coords[1] + 1) not in walked_coords
            ):
                current_coords = (current_coords[0], current_coords[1] + 1)
            else:
                walk = 0
                break
        elif current == ".":
            walk = 0
            break
        else:
            break
        if start_coords in walked_coords and prev != "S":
            walked_coords.remove(start_coords)
        walk += 1
        walked_coords.append(current_coords)
        prev = current
        current = lines[current_coords[0]][current_coords[1]]

    if walk:
        break

furthest_point = walk // 2
print(furthest_point)
