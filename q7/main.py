val_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

hands = list(map(lambda x: x.split(), open("q7/inp.txt").read().splitlines()))


def hand_val(x):
    xmap = {a: x.count(a) for a in set(x)}
    vals = xmap.values()
    if 5 in vals:
        return 5
    if 4 in vals:
        return 4
    if 3 in vals and 2 in vals:
        return 3
    if 3 in vals:
        return 2
    if 2 in vals and len(vals) == 3:
        return 1
    if 2 in vals:
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
