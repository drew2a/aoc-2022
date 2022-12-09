from pathlib import Path

movements = [m.split(' ') for m in Path('input.txt').read_text().split('\n') if m]
directions = {
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
}
head = 0, 0
tails = [head] * 9


def sign(number):
    if not number:
        return 0
    return -1 if number < 0 else 1


places = {head}
for direction, steps in movements:
    n = int(steps)
    dxdy = directions[direction]
    for i in range(n):
        head = head[0] + dxdy[0], head[1] + dxdy[1]
        new_tails = []
        current = head
        for t in tails:
            new_tail = t
            difference = current[0] - t[0], current[1] - t[1]
            if abs(difference[0]) > 1 or abs(difference[1]) > 1:
                new_tail = t[0] + sign(difference[0]), t[1] + sign(difference[1])
            new_tails.append(new_tail)
            current = new_tail
        tails = new_tails
        places.add(tails[-1])

print(f'Count: {len(places)}')
