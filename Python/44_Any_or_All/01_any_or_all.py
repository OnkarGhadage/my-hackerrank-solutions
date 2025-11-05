# Enter your code here. Read input from STDIN. Print output to STDOUT
N, vals = int(input()), list(map(int, input().split()))
print(all(x > 0 for x in vals) and any(str(y) == str(y)[::-1] for y in vals))
