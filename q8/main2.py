from locale import currency
import math


instructions, map_list = open("q8/inp.txt").read().split("\n\n")
mapper = {}
for m in map_list.splitlines():
    k, v = m.split(" = ")
    v = v.strip("()")
    mapper[k] = list(v.split(", "))
total_steps = 0

start_nodes = [x for x in mapper.keys() if x.endswith("A")]
l = len(instructions)
instructions = list(map(lambda x: 1 if x == "R" else 0, instructions))
roundabout = []
for val in start_nodes:
    cnt, index = 0, 0
    current = val

    while not current.endswith("Z"):
        current = mapper[current][instructions[index]]
        index = (index + 1) % l
        cnt += 1

    holding_patt = current
    current = mapper[current][instructions[index]]
    index = (index + 1) % l
    cnt = 1
    while current != holding_patt:
        current = mapper[current][instructions[index]]
        index = (index + 1) % l
        cnt += 1
    roundabout.append(cnt)

print(roundabout)

print(math.lcm(*roundabout))
