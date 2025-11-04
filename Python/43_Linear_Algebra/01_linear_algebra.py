import numpy as np 
N = int(input())
array = np.array([input().split() for _ in range(N)],float)
print(np.around(np.linalg.det(array),2))
