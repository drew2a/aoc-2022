from collections import Counter
from pathlib import Path

content = Path('input.txt').read_text()
counter = Counter(content[:14])
for i in range(14, len(content)):
    if len(+counter) == 14:
        print(i)
        break

    counter.update({content[i]: 1})
    counter.update({content[i - 14]: -1})
