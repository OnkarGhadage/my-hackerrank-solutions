# Problem Statement
## Task
You are given two values a and b.
Perform integer division and print a/b.
## Input Format
The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.
## Constraints
0 < T < 10
## Output Format
Print the value of a/b.
In the case of ZeroDivisionError or ValueError, print the error code.
## Sample Input
`3`  
`10`  
`2 $`  
`31`  
## Sample Output
`Error Code: integer division or modulo by zero`  
`Error Code: invalid literal for int() with base 10: '$'`  
`3`  
<hr>

# My Approach
This problem is like hello world program for exception handling.

I take the input T in first line i.e. the number of test cases are going to be there as input. Then for loop in range of T cause there are going to be T number of test cases.

Inside the for loop I take the input which is in a single line separated by space `a, b = map(str, input().split(" "))`. I take the input outside of try block thats why I take the input in string format.  
You can also try to take the input inside the try block so that you can take input directly in int.  
Like this `a, b = map(int, input().split(" "))`. 

Then write the except block for both `ZeroDivisionError` & `ValueError` and print the error code. 
If there is no exception hit then we print the integer division. 

Division - `a/b` it gives the ans in float data type and Integer division - `a//b` gives answer in integer data type. We need the answer in integer so thats why I implemented Integer division.
