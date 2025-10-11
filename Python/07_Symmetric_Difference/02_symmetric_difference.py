# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
M_values = set(map(int, input().split()))

N = int(input())
N_values = set(map(int, input().split()))

print(*sorted(M_values.symmetric_difference(N_values)), sep='\n')
