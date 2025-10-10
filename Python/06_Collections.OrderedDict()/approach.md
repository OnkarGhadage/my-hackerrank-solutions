# Problem Statement
## Task
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
## Input Format
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.
## Constraints
0 < N <= 100
## Output Format
Print the item_name and net_price in order of its first occurrence.
## Sample Input
`9`  
`BANANA FRIES 12`  
`POTATO CHIPS 30`  
`APPLE JUICE 10`  
`CANDY 5`  
`APPLE JUICE 10`  
`CANDY 5`  
`CANDY 5`  
`CANDY 5`  
`POTATO CHIPS 30`  
## Sample Output
`BANANA FRIES 12`  
`POTATO CHIPS 60`  
`APPLE JUICE 20`  
`CANDY 20`  
<hr>

# My Approach
Read the information give above the problem in HackerRank page.   

Firstly I imported `from collections import OrderedDict` to create a OrderedDict.  

In 5th line Input taken which is number of items stored in N. Then created OrderedDict named orders.   

For loop in range of N.
I get input with item name & price which is space saperated but can't just saperate two items easily using just .split() cause in some cased there are item name is more than two words so split the words and store it in the list. So that we get price by list[-1]. In negative indexing -1 is the last element. Stored the price in price. And then removed the price from the list and joined the remaining list by join function.  

So get the item_name and it's price as well.  

Now in 14th line I write if condition in that if item_name is already in the dict then just add the price to that key's value if not then create new key value pair of item_name and price.  

Lastly print the item and net_price from the dict orders.  

And all done 👍.
