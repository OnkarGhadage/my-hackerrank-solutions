# Problem statement
## Task
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:  
→ A Captain.  
→ An unknown group of families consisting of K members per group where K ≠ 1.  
The Captain was given a separate room, and the rest were given one room per group.  
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room.  
Mr. Anant needs you to help him find the Captain's room number.  
The total number of tourists or the total number of groups of families is not known to you.  
You only know the value of K and the room number list.  
## Input Format
The first line consists of an integer, K. the size of each group.  
The second line contains the unordered elements of the room number list.
## Constraints
1 < K < 1000
## Output Format
Output the Captain's room number.
## Sample Input
`5`  
`1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 `  
## Sample Output
`8`  
<hr>

# My approach
Take inputs:  
In first line contains an integer value which is size of each group.  
In second line the list of room numbers which is unordered.  
The goal is to find the one unique room no. which is the Captain's room number.  

Did in two ways:  
1. Doing manually counting.
2. Use Counters from collections.

Both have same time complexity. For simple approach use Counter and for better understanding use manual way. (Do in both ways).  

1. Initialize a empty dictionary.  
   For loop for every element in list of room numbers `for i in room_no:`.  
   If the number already exist in the dictionary then just increase the value of that key by one `if i in rooms_dict: rooms_dict[i] += 1 `.  
   Else just assign the key value one. `else: rooms_dict[i] = 1`.  

2. `from collections import Counter`  
   Then just pass the list of room numbers to `Counter()` function and all the word will done by the function itself.  


To print the Captain's Room number traverse the full dictionary and if the dict[key] == 1 then it is the Captain's Room print the room number and break from the loop.  

```
for i in room_no:
    if room_no[i] == 1:
        print(i)
        break
```
