# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for _ in range(N):
    print(True if re.fullmatch(r"^[+-]?\d*\.\d+$", input()) else False)
