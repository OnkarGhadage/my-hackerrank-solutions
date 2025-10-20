# Problem statement
## Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.
## Input Format
The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.
## Output Format
Output the total number of students who have subscriptions to both English and French newspapers.
## Sample Input
`9`  
`1 2 3 4 5 6 7 8 9`  
`9`  
`10 1 2 3 11 21 55 6 8`  
## Sample Output
`5`
<hr>

# My approach
First know about the set intersection operation. Intersection gives the common elements from two sets.

Take all input in first line the number studemt who have subscribed to the English newspaper and then in second line the the space separated roll number of student who have subscribed to the English newspaper.  
Same for 3rd and 4th line for French newspaper.

The expected output is the number of student who have subscribed to the both newspaper.  

So do intersection operation on set of roll numbers of English and French newspaper. We get the common roll numbers and then just print the lenght of that set we get the output.

And all done 👍.
