total = 0
with open("q2/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        r, g, b = 0, 0, 0
        line = line[line.index(":") + 1 :]
        line = line.replace(" ", "")
        line = line.replace(";", ",")
        for subset in line.split(","):
            if "red" in subset:
                if (val := int(subset[: subset.index("r")])) > r:
                    r = val
                    continue
            if "blue" in subset:
                if (val := int(subset[: subset.index("b")])) > b:
                    b = val
                    continue
            if "green" in subset:
                if (val := int(subset[: subset.index("g")])) > g:
                    g = val
        # print(line, r, g, b)
        total += r * g * b
    print(total)
