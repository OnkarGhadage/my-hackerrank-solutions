# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
#Column names
columns = input().split()

Student = namedtuple('Student', columns)
sum = 0
for i in range(N):
    #Values
    w, x, y, z = input().split()
    s1 = Student(w, x, y, z)
    sum += int(s1.MARKS)

print(f"{sum/N:.2f}")
