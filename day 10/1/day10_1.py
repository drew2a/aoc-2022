from pathlib import Path

commands = [c.split(' ') for c in Path('input.txt').read_text().split('\n') if c]
cycle = 1
x = 1
states = {}
for command in commands:
    states[cycle] = x
    if command[0] == 'noop':
        cycle += 1
    else:
        states[cycle + 1] = x
        x += int(command[1])
        cycle += 2

s = sum(s * states[s] for s in range(20, cycle, 40))
print(s)
