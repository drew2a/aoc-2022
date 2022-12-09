from pathlib import Path

lines = [line for line in Path('input.txt').read_text().split('\n') if line]

m = []
for line in lines:
    m.append([int(ch) for ch in line])

size = len(m)


def check(row, column):
    def _check(_start):
        n = 0
        for i in range(_start, stop, step):
            n += 1
            if getter(i) >= m[row][column]:
                return False, n
        return True, n

    result = False
    point_score = 1
    for start, getter in [(row, lambda i: m[i][column]), (column, lambda i: m[row][i])]:
        for step, stop in [(-1, -1), (1, size)]:
            found, s = _check(start + step)
            point_score *= s
            if found:
                result = True

    return result, point_score


def _color(text):
    return f'\033[92m{text}\033[0m'


count = 0
scores = set()
for r in range(size):
    line = ''
    for c in range(size):
        correct_tree, score = check(r, c)
        if correct_tree:
            line += _color(m[r][c])
            count += 1
            scores.add(score)
        else:
            line += str(m[r][c])
    print(line)

print(f'Count: {count}')
print(f'Scenic score: {max(scores)}')
