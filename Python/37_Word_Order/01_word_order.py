# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
word = []
for i in range(n):
    word.append(input())
count = Counter(word)
print(len(set(word)))
print(*count.values())
