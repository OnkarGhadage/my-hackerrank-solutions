# Problem Statement
## Task
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.
## Example
Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'
For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not appear in group A, so print -1.
## Expected output:
`1 3`  
`-1`
## Input Format
The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.
## Constraints
1 <= n <= 10000
1 <= m <= 100
1 length of each word in the input < 100
## Output Format
Output m lines.
The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.
<hr>

# My Approach
According to given problem we have two group of letters i.e. A & B. In A there are repeated letters and B have single letters without repetetion. The output is the position of the letters of group B in group A. 

So we imported defaultdict from collections. Using `defaultdict(data_type)` function we created defaultdict. In which we append index for each letter in A for same key. like for `dict[letter].append(index_of_letter)`.

Then we get all the indexes of all letters in dict.
Then finally we print the list of indexes for particular letters from group B. And for those who are not in B but present in A are outputed as -1.

Printed the list using `print(*d[word])`. This prints the list without , & [].

I tried my best to explain. English is not my first language. But if you need any help from me then feel free to reach out.

### Knowledge gained
To print the list in a line we just have to do `print(*list_name)`  
OR  
we can also assign the separater like `print(*list_name, sep = ", ")`
