with open("q5/inp.txt", "r") as inp:
    lines = inp.read()

seeds, *blocks = lines.split("\n\n")
seeds = list(map(int, seeds.split()[1:]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for seed in seeds:
        for d, s, r in ranges:
            if seed in range(s, s + r):
                new.append(d - s + seed)
                break
        else:
            new.append(seed)
    seeds = new

print(min(seeds))
