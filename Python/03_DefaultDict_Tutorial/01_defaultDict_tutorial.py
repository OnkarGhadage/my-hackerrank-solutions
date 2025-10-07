# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split(" "))
grp_a = []
grp_b = []
for i in range(n):
    grp_a.append(input())
for i in range(m):
    grp_b.append(input())

d = defaultdict(list)

for index, word in enumerate(grp_a, start=1):
    d[word].append(index)

for word in grp_b:
    if word in d:
        print(*d[word])
    else:
        print(-1)
