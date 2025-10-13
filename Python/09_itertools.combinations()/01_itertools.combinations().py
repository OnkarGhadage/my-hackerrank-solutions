# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

string, n = input().split()

string = sorted(string)

for i in range(1, int(n)+1):
    sub_str = list(combinations(string,i))

    for j in sub_str:
        print(*j,sep="")
