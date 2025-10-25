# Problem statement
## Task
You are given a space separated list of numbers.  
Your task is to print a reversed NumPy array with the element type float.
## Input Format
A single line of input containing space separated numbers.
## Output Format
Print the reverse NumPy array with type float.
## Sample Input
`1 2 3 4 -8 -10`  
## Sample Output
`[-10.  -8.   4.   3.   2.   1.]`
<hr>

# My approach
Used slicing and dtype.  
To reverse use slicing - `arr[::-1]`  
To change the data type use dtype - `dtype = float`

Direct return the `numpy.array(arr[::-1],dtype='float')`  

And all done 👍.
