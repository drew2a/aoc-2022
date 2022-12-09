from pathlib import Path

lines = [line for line in Path('input.txt').read_text().split('\n') if line]

m = []
for line in lines:
    m.append([int(ch) for ch in line])

size = len(m)


def check(row, column):
    def _check(_start):
        for i in range(_start, stop, step):
            if getter(i) >= m[row][column]:
                return False
        return True

    for start, getter in [(row, lambda i: m[i][column]), (column, lambda i: m[row][i])]:
        for step, stop in [(-1, -1), (1, size)]:
            if _check(start + step):
                return True

    return False


def _color(text):
    return f'\033[92m{text}\033[0m'


count = 0
for r in range(size):
    line = ''
    for c in range(size):
        if check(r, c):
            line += _color(m[r][c])
            count += 1
        else:
            line += str(m[r][c])
    print(line)

print(f'Count: {count}')
