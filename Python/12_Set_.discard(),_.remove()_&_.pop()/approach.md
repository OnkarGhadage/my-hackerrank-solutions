# Problem Statement
## Task
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
## Input Format
The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.
## Constraints
0 < n < 20
0 < N < 20
## Output Format
Print the sum of the elements of set s on a single line.
## Sample Input
`9`  
`1 2 3 4 5 6 7 8 9`  
`10`  
`pop`  
`remove 9`  
`discard 9`  
`discard 8`  
`remove 7`  
`pop`  
`discard 6`  
`remove 5`  
`pop`  
`discard 5`
## Sample Output
`4`  
<hr>

# My Approach 
The first line contains integer value which is number of elements in the set.  
Second line contains the actual values of set.

The third line contains int value which is number of operations we have to operate on the set `s`.  
For loop in range number of operations.

Inside the loop take input of operation and the operand. The some operation have only operation like `pop` and some have operand like `discard 9`.  
And in all test cases there are only single digit numbers as operand so take input as a string and access operand using negative indexing.

if elif elif conditions to check the operation and perform the operation accordingly

Lastly we have to print the sum of elements that remain in the set s. So `print(sum(s))`.

And all done 👍.
