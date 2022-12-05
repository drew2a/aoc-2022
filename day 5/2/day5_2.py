from pathlib import Path

content = [r.split('\n') for r in Path('input.txt').read_text().split('\n\n') if r]
raw_crates, instructions = content
crates = [[] for _ in range(9)]
for line in raw_crates:
    for i, c in enumerate(crates):
        ch = line[1 + i * 4]
        if ch != ' ' and not ch.isnumeric():
            c.append(ch)

for instruction in instructions:
    if not instruction:
        continue
    tokens = instruction.split(' ')
    count = int(tokens[1])
    _from = int(tokens[3]) - 1
    _to = int(tokens[5]) - 1

    moving = crates[_from][:count]
    crates[_from] = crates[_from][count:]
    crates[_to] = moving + crates[_to]

result = ''
for c in crates:
    result += c[0]

print(result)
