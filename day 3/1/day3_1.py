import string
from itertools import islice
from pathlib import Path

rucksacks = {r for r in Path('./input.txt').read_text().split('\n') if r}
alphabet = {key: value for value, key in enumerate(string.ascii_lowercase + string.ascii_uppercase, 1)}
score = 0
for r in rucksacks:
    middle = len(r) // 2
    left_compartment = set(islice(r, 0, middle))

    for char in islice(r, middle, len(r)):
        if char in left_compartment:
            score += alphabet[char]
            break

print(score)
