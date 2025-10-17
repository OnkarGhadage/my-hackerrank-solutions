# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
deq = deque()
N = int(input())
for i in range(N):
    operation = input().split()
    if operation[0] == "append":
        deq.append(operation[-1])
    elif operation[0] == "appendleft":
        deq.appendleft(operation[-1])
    elif operation[0] == "pop":
        deq.pop()
    elif operation[0] == "popleft":
        deq.popleft()

print(*deq)
