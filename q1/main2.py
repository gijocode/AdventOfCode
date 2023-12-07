total = 0
with open("q1/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        first_no, last_no = 0, 0
        line=line.strip()
        for i in range(len(line)+1):
            if not first_no and line[i].isdigit():
                first_no = int(line[i])
            if not last_no and line[-i].isdigit() and i:
                last_no = int(line[-i])
            if first_no and last_no:
                break
        print(line, first_no, last_no)
        total += (first_no * 10) + last_no
print(total)
