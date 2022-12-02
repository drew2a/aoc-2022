from pathlib import Path

rounds = [r.split(' ') for r in Path('./input.txt').read_text().split('\n') if r]
elf_index = {'A': 0, 'B': 1, 'C': 2}
score_index = {'X': 0, 'Y': 3, 'Z': 6}
you_turn = {
    'X': lambda elf: (elf - 1) % 3,
    'Y': lambda elf: elf,
    'Z': lambda elf: (elf + 1) % 3,
}

score = 0
for elfie, you in rounds:
    elf_i = elf_index[elfie]
    turn = you_turn[you](elf_i)
    score += turn + 1
    score += score_index[you]

print(score)
