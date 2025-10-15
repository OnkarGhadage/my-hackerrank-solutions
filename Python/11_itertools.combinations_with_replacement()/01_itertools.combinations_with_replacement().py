# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
string, K = input().split()

for i in list(combinations_with_replacement(sorted(string), int(K))):
    for j in i:
        print(j,end="")
    print()
