t = int(input().strip())
for _ in range(t):
    temp1=1 
    temp2=1 
    sum=0
    n = int(input().strip())
    while temp1 < n:
        temp1, temp2 = temp2, temp1+temp2
        if temp1%2 == 0 and temp1<n:
            sum+=temp1
    print(sum)