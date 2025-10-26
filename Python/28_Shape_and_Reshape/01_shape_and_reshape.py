import numpy
arr = list(map(int, input().split()))
np_arr = numpy.array(arr)
print(np_arr.reshape(3,3))
