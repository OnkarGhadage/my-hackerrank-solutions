import numpy as np 
N = int(input())
arr1 = []
array1 = np.array([input().split() for _ in range(N)],dtype = int)
array2 = np.array([input().split() for _ in range(N)],dtype = int)

print(np.dot(array1,array2))
# OR
print(np.matmul(array1,array2))
# OR
print(array1 @ array2)
