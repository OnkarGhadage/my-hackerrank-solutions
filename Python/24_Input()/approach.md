# Problem statement
## Task
You are given a polynomial P of a single indeterminate (or variable), z.
You are also given the values of x and k. Your task is to verify if P(x) = k
## Constraints
All coefficients of polynomial P are integers.
x and y are also integers.
## Input Format
The first line contains the space separated values of æ and k.
The second line contains the polynomial P.
## Output Format
Print True if P(x)=k. Otherwise, print False.
## Sample Input
`1 4`  
`x ^ 3 + x ^ 2 + x + 1`  
## Sample Output
`True`  
## Explanation
P(1) = 1 ^ 3 + 1 ^ 2 + 1 + 1 = 4 = k
Hence, the output is True.
<hr>

# My approach
Take input in first line a space separated two integer's x and k.  
In second line a string input which is a expression or Pass it directly in a eval function - `eval(input())`.  
The eval() function return a value store it or directly use it in if condition like `if eval(input()) == k`.  
Print `True` if the result of expression is equal to the k (Second input number in first line) otherwise `False`.  

And all done 👍.
