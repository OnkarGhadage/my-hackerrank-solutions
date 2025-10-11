# Problem Statement
## Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
## Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.
## Output Format
Output the symmetric difference integers in ascending order, one per line.
## Sample Input
`STDIN       Function`  
`-----       --------`  
`4           set a size M = 4`  
`2 4 5 9     a = {2, 4, 5, 9}`  
`4           set b size N = 4`  
`2 4 11 12   b = {2, 4, 11, 12}`  
## Sample Output
`5`  
`9`  
`11`  
`12`  
<hr>

# My Approach
First file I write first without any help and without any search and second one is after some research.  

In first file I take input `M` as int. Initilize `setM` as set. The `M` values of set M are stored in `Mvalues_list`. Then I updated the `setM` by updating Mvalues_list.  

Same procedure for the set N also.

Then I used very easy and simple formula for symmetric difference `(setM.difference(setN)).union(setN.difference(setM))`. 

Symmetric difference is like (A - B) U (B - A).

Then we get all the values of symmetric difference but we have to print the values in sorted order. For that I I converted difference list into a list. Then map function to convert all numbers convert from str to int. Then sort the list and print.

Print like `print(*diff_list, sep='\n')` it iterates full list and prints every value just added a `sep='/n'` to print every new value in new line.

And all done 👍.
