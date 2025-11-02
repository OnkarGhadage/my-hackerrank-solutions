# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools  import combinations
N = int(input())
letters = input().split()
K = int(input())
combinations = list(combinations(letters,K))
count = 0
for i in combinations:
  if "a" in i:
    count += 1 
print(count/len(combinations))
