t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    i = 2
    max = 1 
    while i * i <= n:
        while n % i == 0:
            max = i 
            n = n//i
        i+=1 
    if n > 1:
        max = n
    print(max)
