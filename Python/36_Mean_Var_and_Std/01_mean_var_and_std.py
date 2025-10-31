import numpy as np
N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
array = np.array(A)
print(np.mean(array,axis=1))
print(np.var(array,axis=0))
print(np.round(np.std(array),11))
