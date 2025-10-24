# Enter your code here. Read input from STDIN. Print output to STDOUT
A = input()
listA = set(map(int , input().split()))
N = int(input())
for i in range(N):
    ope, leng = input().split()
    if ope in "update":
        listA.update(set(map(int , input().split())))
    elif ope in "intersection_update":
        listA.intersection_update(set(map(int , input().split())))
    elif ope in "difference_update":
        listA.difference_update(set(map(int , input().split())))
    elif ope in "symmetric_difference_update":
        listA.symmetric_difference_update(set(map(int , input().split())))
print(sum(listA))
