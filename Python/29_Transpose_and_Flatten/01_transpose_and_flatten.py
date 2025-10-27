import numpy as np 

n, m = map(int, input().split())
list_ = []
for i in range(n):
    list_.append(list(map(int, input().split())))
arr = np.array(list_)
print(arr.transpose())
print(arr.flatten())
