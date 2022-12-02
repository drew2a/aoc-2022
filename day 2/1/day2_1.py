from pathlib import Path

rounds = [r.split(' ') for r in Path('./input.txt').read_text().split('\n') if r]
elf_index = {'A': 0, 'B': 1, 'C': 2}
you_index = {'X': 0, 'Y': 1, 'Z': 2}

score = 0
for elf, you in rounds:
    elf_i = elf_index[elf]
    you_i = you_index[you]
    score += you_i + 1
    if elf_i == you_i:
        score += 3
    elif you_i == (elf_i + 1) % 3:
        score += 6
print(score)
