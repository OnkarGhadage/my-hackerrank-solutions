# Problem Statement
## Task
You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
For a better understanding of the problem, check the explanation.
## Input Format
A single line of input consisting of the string .
## Output Format
A single line of output consisting of the modified string.
## Constraints
All the characters of  denote integers between  and .

## Sample Input
`1222311`
## Sample Output
`(1, 1) (3, 2) (1, 3) (2, 1)`
## Explanation
First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.
<hr>

# My approach
`import itertools` we need the groupby function

take input I applyed the itertools.groupby() on input() directly like itertools.groupby(input()).

Then for loop for key value of groupby dict. Just printed in expected format using f string.  
`print(f"({len(list(group))}, {key})",end=" ")`

And all done 👍.
