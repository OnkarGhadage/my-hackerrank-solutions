# This solution is written and tested by me
n = int(input())
s = set(map(int, input().split()))
m = int(input())

for i in range(m):
    operation = input()
    if "pop" in operation:
        s.pop()
    elif "remove" in operation:
        s.remove(int(operation[-1]))
    elif "discard" in operation:
        s.discard(int(operation[-1]))

print(sum(s))
