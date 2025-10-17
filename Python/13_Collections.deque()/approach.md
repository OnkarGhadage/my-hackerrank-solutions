# Problem Statement
## Task
Perform append, pop, popleft and appendleft methods on an empty deque d.
## Input Format
The first line contains an integer N. the number of operations.
The next N lines contains the space separated names of methods and their values.
## Constraints
0 < N <= 100
## Output Format
Print the space separated elements of deque d.
## Sample Input
`6`  
`append 1`  
`append 2`  
`append 3`  
`appendleft 4`  
`pop`  
`popleft`  
## Sample Output
`12`  
<hr>

# My Approach 
Firstly know some theory of deque. Deque means double ended queue. As per name it is double ended mean adding and removing elements are possible on both the ends of queue thats why deque.

So for the deque `import from collections import deque` for adding and removing element from the both sides of the queue.

Then initilized the dqu as deque. Take N input as int which is the number of operations that have to be performed on deque.

For loop in range of N. Then take the input the operation and operand in single line. Taken the input in list named operation. In that operation is in 0th index and operand is at 1st or -1th index.

So then a if,elif.. conditions for each operation.  
`    if "append" in operation:`  
`        deq.append(operation[-1])`  
Like this...

And all done 👍.
