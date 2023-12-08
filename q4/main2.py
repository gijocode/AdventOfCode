lines = []
win_map = {}

with open("q4/inp.txt", "r") as inpfile:
    for line in inpfile.readlines():
        lines.append(line[line.index(":") + 1 :].strip())

for n, line in enumerate(lines):
    winner_nos, elf_nos = line.split("|")
    winner_nos = [int(x) for x in winner_nos.split(" ") if x]
    elf_nos = [int(x) for x in elf_nos.split(" ") if x]
    matches = [x for x in elf_nos if x in winner_nos]
    win_map[str(n + 1)] = [str(x) for x in range(n + 2, n + 2 + len(matches))]

cards = list(win_map.keys())
n = 0
while n < len(cards):
    current_no = cards[n]
    cards.extend(win_map[current_no])
    n += 1
print(len(cards))
# Ans 13080971
