import time
from itertools import permutations

st = time.perf_counter()
lines = [x.split() for x in open("q12/inp.txt").read().splitlines()]
total = 0
for line in lines:
    print(line)
    report, working_no = line
    words = []
    word_split = working_no.split(",")
    num_split = list(map(int, word_split))

    words.extend(["."] * (len(report) - sum(num_split)))

    # print(["."] * (len(report) - ((sum(num_split) * 2) - 2)))
    for i, word in enumerate(word_split):
        if i == 0:
            words.append("#" * int(word))
        elif i == len(word_split) - 1:
            words.append("#" * int(word))
        else:
            words.append("#" * int(word))

    word_list = set(x for x in permutations(words))
    l = list(word_list)[-1]
    word_list = [
        x
        for i, x in enumerate(list(word_list)[:-1])
        if "#" not in x and "#" not in list(word_list)[i + 1]
    ]
    word_list.append(l)
    print(word_list)

    for i, x in enumerate(report):
        word_list = [
            "".join(word) for word in word_list if (x == "?" or list(word)[i] == x)
        ]
    word_list = [
        x
        for x in word_list
        if [y for y in list(map(len, x.split("."))) if y] == num_split
    ]
    total += len(word_list)

print(total)

print(f"took {(time.perf_counter() - st)*1000:0.4f}ms")
