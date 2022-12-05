from pathlib import Path

pairs = [r.split(',') for r in Path('./input.txt').read_text().split('\n') if r]
score = 0
for p in pairs:
    def _in(p1, p2):
        return p1[0] <= p2[0] <= p1[1] and p1[0] <= p2[1] <= p1[1]


    first = [int(i) for i in p[0].split('-')]
    second = [int(i) for i in p[1].split('-')]
    if _in(first, second) or _in(second, first):
        score += 1

print(score)  # 536 too low
