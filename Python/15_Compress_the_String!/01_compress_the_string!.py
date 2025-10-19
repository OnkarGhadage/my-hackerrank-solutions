import itertools
numbers = itertools.groupby(input())
for key, group in numbers:
    print(f"({len(list (group))}, {key})", end=" ")
