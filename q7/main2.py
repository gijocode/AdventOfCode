val_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 11,
    "9": 10,
    "8": 9,
    "7": 8,
    "6": 7,
    "5": 6,
    "4": 5,
    "3": 4,
    "2": 3,
    "J": 2,
}

hands = list(map(lambda x: x.split(), open("q7/inp.txt").read().splitlines()))


def hand_val(x):
    xmap = {a: x.count(a) for a in set(x)}
    vals = xmap.values()
    keys = xmap.keys()
    if 5 in vals:
        return 5
    if 4 in vals:
        if "J" in keys:
            return 5
        return 4
    if 3 in vals and 2 in vals:
        if "J" in keys:
            return 5
        return 3
    if 3 in vals:
        if "J" in keys:
            return 4
        return 2
    if 2 in vals and len(vals) == 3:
        if "J" in keys:
            return 4 if xmap["J"] == 2 else 3
        return 1
    if 2 in vals:
        if "J" in keys:
            return 2
        return 0
    if "J" in keys:
        return 0
    return -1


def greater_hand(x, y):
    if hand_val(x[0]) > hand_val(y[0]):
        return True
    if hand_val(y[0]) > hand_val(x[0]):
        return False
    for a, b in zip(x[0], y[0]):
        if a != b:
            return val_map[a] > val_map[b]
    return False


for i in range(len(hands) - 1):
    swapped = False
    for j in range(len(hands) - 1 - i):
        if greater_hand(hands[j], hands[j + 1]):
            temp = hands[j]
            hands[j] = hands[j + 1]
            hands[j + 1] = temp
            swapped = True
    if not swapped:
        break

total = 0
for i, v in enumerate(hands):
    total += (i + 1) * int(v[1])
print(total)
