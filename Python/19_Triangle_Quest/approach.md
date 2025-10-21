# Problem statement
You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
1
22
333
4444
55555
Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
Note: Using anything related to strings will give a score of 0.
## Input Format
A single line containing integer. N.
## Constraints
1 <= N <= 9
## Output Format
Print N-1 lines as explained above.
## Sample Input
`5`  
## Sample Output
`1`  
`22`  
`333`  
`4444`  
<hr>

# My approach
Its just an mathametical problem. We have to just multiple each number by 1, 11, 111, 1111... and so on for 1, 2, 3, 4... respectively.

And to get that 1, 11, 111, 1111... we need to just divide 10,100,1000... by 9 and we get 1, 11, 111...

So for each iteration we get the i'th power of 10 and divide it by 9. We get 1,11,111... 

Lastly multiply the i to it

`(10**i//9)*i`

And all done 👍.
