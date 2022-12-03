import string
from pathlib import Path

rucksacks = [set(r) for r in Path('./input.txt').read_text().split('\n') if r]
alphabet = {key: value for value, key in enumerate(string.ascii_lowercase + string.ascii_uppercase, 1)}
score = 0
for i in range(0, len(rucksacks), 3):
    common = rucksacks[i] & rucksacks[i + 1] & rucksacks[i + 2]
    badge = common.pop()
    score += alphabet[badge]

print(score)
