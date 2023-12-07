total = 0
num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
with open("q1/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        int_map = {v: k for k in num_map.keys() if ((v := line.find(k)) != -1)}
        for k in num_map.keys():
            if line.count(k) > 1:
                int_map[line.rfind(k)] = k
        first_no, last_no = 0, 0
        line = line.strip()
        for i in range(len(line) + 1):
            if not first_no and line[i].isdigit():
                first_no = (
                    num_map[int_map[m]]
                    if int_map and ((m := min(int_map.keys())) < i)
                    else int(line[i])
                )
            if not last_no and line[-i].isdigit() and i:
                last_no = (
                    num_map[int_map[m]]
                    if int_map and ((m := max(int_map.keys())) > (len(line) - i))
                    else int(line[-i])
                )
            if first_no and last_no:
                break
        # print(line, first_no, last_no)
        # print(int_map)
        total += (first_no * 10) + last_no
    print(total)
