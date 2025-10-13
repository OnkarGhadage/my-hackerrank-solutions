# Problem Statement

## Task
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
## Input Format
A single line containing the string S and integer value k separated by a space.
## Constraints
0 <= k <= len(S)
The string contains only UPPERCASE characters.
## Output Format
Print the different combinations of string S on separate lines.
## Sample Input
`HACK 2`
## Sample Output
`A`  
`C`  
`H`  
`K`  
`AC`  
`AH`  
`AK`  
`CH`  
`CK`  
`HK`  
<hr>

# My Approach  

It is quite similar problem that we solved earlier. In that we just have to print secified number of combination. But in this we have to print combination till the number.

Firstly `from itertools import combinations`.

Then we take input string and number is one line by `string, n = input().split()`. Input is splited by default by ' ' (space). If you want to specify the separater then `split(',')` (, comma is the separated).

Then we sort the string cause we want the combinations in sorted order.

Then for loop from 1 to n+1. we create `sub_str` list of string combinations of i numbers. It will create combinations of words from 1 to n.

Then after making the combination we have to print it in every new line. So nested for loop for every set in sub_str. The seb_str is list but the combinations are stored in set form.  
Then `print(*j,sep="")`. Print every element in the set of list with separator `""` (nothing).


And all done 👍.
