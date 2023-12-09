time, distance = open("q6/inp.txt").read().split("\n")[:-1]
time = list(map(int, time.split()[1:]))
distance = list(map(int, distance.split()[1:]))

total_win = 1
for time_limit, dist in zip(time, distance):
    beat_ways = 0
    for t in range(time_limit // 2, 1, -1):
        # print("hi")
        # print((time_limit - t) * t)
        if dist >= (time_limit - t) * t:
            break
        beat_ways += 1
    beat_ways = beat_ways * 2 if time_limit % 2 else beat_ways * 2 - 1
    print(beat_ways)
    if beat_ways:
        total_win *= beat_ways
print(total_win)
