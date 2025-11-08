# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

for _ in range(N):
    number = input()
    check = re.fullmatch(r'[789]\d{9}', number)
    if check:
      print("YES")
    else:
      print("NO")
