# Problem Statement
## Task
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
## Input Format
A single line containing the space separated string S and the integer value k.
## Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.
## I/O
#### Sample Input
`HACK 2`
#### Sample Output
`AC`  
`AH`  
`AK`  
`CA`  
`CH`  
`CK`  
`HA`  
`HC`  
`HK`  
`KA`  
`KC`  
`KH`

# My Approach

Firstly I took the input which is saperated by space string and value.
Then splited it and stored in two variables i.e. string & n.  

Create a list.
And apply the permutation function on string with n value `permutations(string,n)`.
And store as list in `my_list` (`list(permutations(string,n))`).

Then printed in required format.

And all done 👍.


Used intresting thing i.e. `print("....",end="")`.
Where we can assign the end part of the print function.
