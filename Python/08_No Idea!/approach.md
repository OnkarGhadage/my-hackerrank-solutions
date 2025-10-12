# Problem Statement
## Task
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i∈ A, you add 1 to your happiness. If i ∈ B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
## Constraints
1 <= n <= 10 ^ 5
1 <= m <= 10 ^ 5
1< Any integer in the input < 109
## Input Format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.
## Output Format
Output a single integer, your total happiness.
## Sample Input
`3 2`  
`1 5 3`  
`3 1`  
`5 7`  
## Sample Output
`1`
## Explanation
You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7
in set B does not exist in the array so it is not included in the calculation.
Hence, the total happiness is 2-1-1.
<hr>

# My Approach
This is very intresting problem to solve.  

We just have to calculate the happiness score. If the array contain the liked number the happiness score increase by 1 and for dislike number the score decrease by 1 as simple as that.  

As input format I take the N & M input in first line by map and split function `n, m = map(int, input().split())`.   
Then read the N numbered array in second line like `array = list(map(int,input().split()))`. This array can have dublicate numbers and thats I stored it in list type. If I store it in set the dublicate numbers can vanish and if affect the happiness core.

Then next two line contain like and dislike numbers. So we just need the number so that I stored it in set type cause the duplicate numbers can increase the space and time complexity. We just need the number is liked or disliked.

Initilized the `happiness = 0`.

For loop to element in array and if the number in array is in like then `happiness += 1` which is equivalent to `happiness = happiness + 1`.

The main line is elif condition cause I earlier written the `else: happiness -= 1` and it cause the test case failuer. And also for fast execution I changed the like and dislike to set from list.

So I write `elif i in dislike: happiness -= 1` because of that the happiness score only get decrease by 1 when the number is in dislike. It prevents from the number which id not in liked and disliked as well.

And all done 👍.
