from pathlib import Path

commands = [c.split(' ') for c in Path('input.txt').read_text().split('\n') if c]
cycle = 1
x = 1
states = {0: 1}
for command in commands:
    states[cycle] = x
    if command[0] == 'noop':
        cycle += 1
    else:
        states[cycle + 1] = x
        x += int(command[1])
        cycle += 2

i = 1
j = 0
line = ''
while i < cycle:
    value = states[i]
    ch = '#' if value - 2 < i - j - 1 < value + 2 else '.'
    line += ch

    if not (i % 40):
        print(line)
        line = ''
        j += 40

    i += 1
