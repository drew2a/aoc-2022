from pathlib import Path
from types import SimpleNamespace

content = Path('input.txt').read_text().split('\n')
dir_content = []
root = SimpleNamespace(files={}, dirs={})
current = root
for line in content:
    if not line:
        continue
    tokens = line.split(' ')

    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '/':
                current = root
            else:
                current = current.dirs[tokens[2]]
        elif tokens[1] == 'ls':
            ...
    else:
        name = tokens[1]
        if tokens[0] == 'dir':
            current.dirs[name] = SimpleNamespace(files={}, dirs={'..': current})
        else:
            current.files[name] = int(tokens[0])

result = 0


def tree_traverse(r, level=0):
    global result
    total = 0

    starter = ' ' * level * 4

    for name, size in r.files.items():
        print(f'{starter}-{name}({size})')
        total += size

    for name, d in r.dirs.items():
        if name == '..':
            continue
        print(f'{starter}-{name}(dir)')
        one_dir_size = tree_traverse(d, level + 1)
        if one_dir_size < 100000:
            result += one_dir_size
        print(f'{starter}    size: {one_dir_size}')
        total += one_dir_size

    return total


tree_traverse(root)

print(f'Result: {result}')