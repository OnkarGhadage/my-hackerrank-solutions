import numpy as np 

N, M = map(int, input().split())
a, b = [], []
for i in range(N):
  a.append(list(map(int, input().split())))
for i in range(N):
  b.append(list(map(int, input().split())))
A = np.array(a)
B = np.array(b)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
