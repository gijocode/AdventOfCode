instructions, map_list = open("q8/inp2.txt").read().split("\n\n")
mapper = {}
for m in map_list.splitlines():
    k, v = m.split(" = ")
    v = v.strip("()")
    mapper[k] = list(v.split(", "))
total_steps, index = 0, 0
val = "AAA"
"""
while val != "ZZZ":
    total_steps += 1
    val = mapper[val][0 if instructions[0] == "L" else 1]
    instructions = instructions[1:] + instructions[0]
print(total_steps)
"""
l = len(instructions)
instructions = list(map(lambda x: 1 if x == "R" else 0, instructions))
print(instructions)
print(mapper)
while not val == "ZZZ":
    val = mapper[val][instructions[index]]
    index = (index + 1) % l
    print(val, index)
    total_steps += 1
    # print("Finding Z for ", val, current)
print(total_steps)
