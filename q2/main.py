total = 0
with open("q2/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        game_no = int(line[4 : line.index(":")])
        line = line[line.index(":") + 1 :].strip()
        line = line.replace(" ", "")
        line = line.replace(";", ",")
        for subset in line.split(","):
            if "red" in subset:
                if int(subset[: subset.index("r")]) > 12:
                    break
            if "blue" in subset:
                if int(subset[: subset.index("b")]) > 14:
                    break
            if "green" in subset:
                if int(subset[: subset.index("g")]) > 13:
                    break
        else:
            total += game_no
            print(line)
    print(total)
