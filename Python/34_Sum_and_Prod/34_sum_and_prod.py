import numpy as np

N, M = map(int, input().split())    # Take space saparated two integer input
A = []    # Make a empty list
for i in range(N):
  A.append(list(map(int, input().split())))    # Append the each row into the list
array = np.array(A)    # Create the numpy array
array = np.sum(A,axis=0)    # Make a array sum along axis 0
print(np.prod(array))    # print the product of the sum. No axis specified then all numbers product -> single value 
