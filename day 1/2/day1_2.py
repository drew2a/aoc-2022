import heapq
from pathlib import Path

groups = Path('./input.txt').read_text().split('\n\n')
groups = (group.split('\n') for group in groups)
groups = (sum(int(item) for item in group if item) for group in groups)
top_three = sum(heapq.nlargest(3, groups))
print(top_three)
