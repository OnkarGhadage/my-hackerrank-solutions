import numpy as np

N, M = map(int, input().split())    # Take two space separated int values. Rows, Column
A = []    #Make a empty list
for i in range(N):
  A.append(list(map(int, input().split())))    # Append the row elements in A list
array = np.array(A)    # Make list A a numpy array
array = np.min(array, axis=1)    # Find the min value over axis 1
print(np.max(array))    # Print the max value (No axis needed for 1D array)
