inp = open("q15/inp.txt").read().strip()
words = inp.split(",")
final_total = 0
for word in words:
    total = 0
    for letter in word:
        total += ord(letter)
        total *= 17
        total %= 256
    final_total += total
print(final_total)
