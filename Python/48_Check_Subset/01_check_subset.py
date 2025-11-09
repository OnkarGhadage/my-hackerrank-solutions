# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    N = int(input())
    A = set(map(int, input().split()))
    M = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))
