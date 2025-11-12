# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
is_ = True
for i in range(n):
    N = set(map(int, input().split()))
    if not A > N:
        is_ = False
print(is_)
