lines = []
with open("q4/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        lines.append(line[line.index(":") + 1 :].strip())
total = 0
for line in lines:
    winner_nos, elf_nos = line.split("|")
    winner_nos = [int(x) for x in winner_nos.split(" ") if x]
    elf_nos = [int(x) for x in elf_nos.split(" ") if x]
    matches = [x for x in elf_nos if x in winner_nos]
    if matches:
        total += pow(2, len(matches) - 1)
print(total)
