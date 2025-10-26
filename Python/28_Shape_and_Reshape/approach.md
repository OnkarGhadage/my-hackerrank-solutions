# Problem statement 
## Task
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
## Input Format
A single line of input containing  space separated integers.
## Output Format
Print the 3X3 NumPy array.
## Sample Input
`1 2 3 4 5 6 7 8 9`  
## Sample Output
`[[1 2 3]`  
` [4 5 6]`  
` [7 8 9]]`  
<hr>

# My approach
`import numpy`  

Take input in single line which is 9 integer values. - `arr = list(map(int, input().split()))`  

Then just convert the python list into a numpy array. - `np_arr = numpy.array(arr)`  

Last step convert the numpy array shape from 1D to 3D with shape 3 X 3. - `np_arr.reshape(3,3)`  

Print the reshaped array. `print(np_arr.reshape(3,3))`

And all done 👍.
