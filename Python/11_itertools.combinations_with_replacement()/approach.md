# Problem Statement
## Task
You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
## Input Format
A single line containing the string S and integer value k separated by a space.
## Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.
## Output Format
Print the combinations with their replacements of string S on separate lines.
## Sample Input
HACK 2`  
## Sample Output
`AA`  
`AC`  
`AH`  
`AK`  
`CC`  
`CH`  
`CK`  
`HH`  
`HK`  
`KK`  
<hr>

# My Approach 
This problem is very similar problem to the one I pushed earlier which is itertools.combinations(). [Check here](09_itertools.combinations()).

Firstly `from itertools import combinations_with_replacement`.

Then take input string and number which is separated by space. `string, K = input().split()` First is string and second one is number.

Then I run for loop for element in `list(combinations_with_replacement(sorted(string), int(K)))`.  
`combinations_with_replacement(sorted(string), int(K))` This creates the tuple of every combination so I make it list.  

Then a nested for loop for particular tuple i.e. a combination and print the letters in the tuple in a single line by using `end=""`.

And all done 👍.
