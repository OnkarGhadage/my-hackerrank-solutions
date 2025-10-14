# Problem Statement
## Task
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.
## Input Format
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.
## Constraints
0 < N < 1000
## Output Format
Output the total number of distinct country stamps on a single line.
## Sample Input
`7`  
`UK`  
`China`  
`USA`  
`France`  
`New Zealand`  
`UK`  
`France`  
## Sample Output
`5` 
## Explanation
UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).
<hr>

# My Approach  
Very easy problem.  

Take N integer input in first line. Which is the number of stamps Rupal have we just have to find out how many countries stamp he/she have. The N is not the expected output cause Rupal can have two or many stamp of one country so we have to calculate that.  

Initilize the set stamps like `stamps = set()`. 

Then for loop in range of N i.e. number of stamps Rupal have. Then just add the input to stamps so that duplicate countries will be removed and data will be distinct.

Lastly print the length of stamps `len(stamps)`.

And all done 👍.
