time, distance = open("q6/inp.txt").read().split("\n")[:-1]
time = int("".join(time.split()[1:]))
distance = int("".join(distance.split()[1:]))

beat_ways = 0
for t in range(time // 2, 1, -1):
    if distance >= (time - t) * t:
        break
    beat_ways += 1
beat_ways = beat_ways * 2 if time % 2 else beat_ways * 2 - 1
print(beat_ways)
