# Problem Statement
## Task
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.
Average = Sum of all marks Total Students
### Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
## Input Format
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, name and class, under their respective column names.
## Constraints
0 < N <= 100
## Output Format
Print the average marks of the list corrected to 2 decimal places.
## Sample Input
`5`  
`ID         MARKS      NAME       CLASS     `  
`1          97         Raymond    7         `  
`2          50         Steven     4         `  
`3          91         Adrian     9         `  
`4          72         Stewart    5         `  
`5          80         Peter      6   `  
## Sample Output
`78.00`  
<hr>

# My Approach
`from collections import namedtuple`  
Read the info provided by HackerRank it is issential to solve the problem.  

Take input in 5th line of N which is total number of student. Afterwards the multiple space saperated column names. Which are split and stored in list named columns.
Then created namedtuple named Student with typename Student and fields are ID, MARKS, NAME, CLASS.

Initialize sum = 0. Run for loop in range of N. In that we take input of values in sequence of given column names. Stored in W, X, Y, Z and stored in Student namedtuple for s1. s1 is like student.
Then add the marks in sum of that student. For every iteration loop takes all N students values and add marks to the sum.

Lastly printed the average of marks. Just one things is that required average needs 2 digits after decimal points so used f string `f"{sum/N:.2f}"` to print two digits after decimal points.

And all done 👍.
