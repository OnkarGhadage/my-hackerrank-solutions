# Problem Statement
## Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
## Input Format
The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
## Constraints
0 < Total number of students in college < 1000
## Output Format
Output the total number of students who have at least one subscription.
## Sample Input
`9`  
`1 2 3 4 5 6 7 8 9`  
`9`  
`10 1 2 3 11 21 55 6 8`  
## Sample Output
`13`
<hr>

# My Approach 
Read about the union operation first. It is a simple mathamatics term.  

In first line take input of number of student who have subscribed to the English newspaper stored in `n` and next line contain input of roll numbers of student who have subscription of English news paper stored in `english` in `set` data type.  
In third line take input of number of student who have subscribed to the French newspaper stored in `m` and next line contain input of roll numbers of student who have subscription of French news paper stored in `french` in `set` data type.  

Take all inputs in `integer` and the roll numbers in `set` format. Cause we have to perform set operation on it.

Now expected output is the total number of students who have at least one subscription. Mean we have to print the total number of student given as roll number for subscription.

For that perform union operation on both sets English and French and length of that union set is the expected output i.e. the total number of students who have at least one subscription.

And all done 👍.
