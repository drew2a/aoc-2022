from collections import Counter
from pathlib import Path

content = Path('input.txt').read_text()
counter = Counter(content[:4])
for i in range(4, len(content)):
    if len(+counter) == 4:
        print(i)
        break

    counter.update({content[i]: 1})
    counter.update({content[i - 4]: -1})
