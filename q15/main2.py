inp = open("q15/inp.txt").read().strip()
words = inp.split(",")


def get_hash(word):
    total = 0
    for letter in word:
        total += ord(letter)
        total *= 17
        total %= 256
    return total


hmap = {}
boxes = [{} for _ in range(256)]
for word in words:
    label, lens = word.split("=") if word[-1].isdigit() else (word[:-1], 0)
    if label not in hmap:
        hmap[label] = get_hash(label)
    hash_val = hmap[label]
    if lens:
        boxes[hash_val][label] = lens
    elif boxes[hash_val].get(label):
        del boxes[hash_val][label]

total_power = 0
for i, box in enumerate(boxes):
    for j, (_, power) in enumerate(box.items()):
        total_power += (i + 1) * (j + 1) * int(power)

print(total_power)
