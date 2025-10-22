# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
e = set(input().split())
m = input()
f = set(input().split())
print(len(e.symmetric_difference(f)))
