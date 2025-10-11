# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
setM = set()
Mvalues_list = input().split()
setM.update(Mvalues_list)

N = int(input())
setN = set()
Nvalues_list = input().split()
setN.update(Nvalues_list)
    
difference = (setM.difference(setN)).union(setN.difference(setM))

diff_list = list(difference)
diff_list = list(map(int, diff_list))
diff_list.sort()
print(*diff_list, sep='\n')
