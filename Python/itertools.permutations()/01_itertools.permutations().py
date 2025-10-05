# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

inp = input().split(" ")

string = sorted(inp[0])
n = int(inp[1])

my_list = list(permutations(string,n))

for i in my_list:
    for s in range(n):
        print(i[s],end="")
    print()
