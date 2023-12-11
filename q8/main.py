instructions, map_list = open("q8/inp2.txt").read().split("\n\n")
mapper = {}
for m in map_list.splitlines():
    k, v = m.split(" = ")
    v = v.strip("()")
    mapper[k] = list(v.split(", "))

total_steps, index = 0, 0
val = "AAA"
l = len(instructions)
instructions = list(map(lambda x: 1 if x == "R" else 0, instructions))

while not val == "ZZZ":
    val = mapper[val][instructions[index]]
    index = (index + 1) % l
    total_steps += 1
print(total_steps)
