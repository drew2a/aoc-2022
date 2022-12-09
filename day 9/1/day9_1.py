from pathlib import Path

movements = [m.split(' ') for m in Path('input.txt').read_text().split('\n') if m]
directions = {
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
}
head = tail = 0, 0


def sign(number):
    if not number:
        return 0
    return -1 if number < 0 else 1


places = {tail}
for direction, steps in movements:
    n = int(steps)
    dxdy = directions[direction]
    for i in range(n):
        head = head[0] + dxdy[0], head[1] + dxdy[1]
        difference = head[0] - tail[0], head[1] - tail[1]

        if abs(difference[0]) > 1 or abs(difference[1]) > 1:
            tail = tail[0] + sign(difference[0]), tail[1] + sign(difference[1])
            places.add(tail)

print(f'Count: {len(places)}')
