t = int(input().strip())
sum = 0
for _ in range(t):
    n = int(input().strip())
    def sum_(k):
        no_of_multiple = (n-1) // k
        sum_of_multiple = k * (no_of_multiple * (no_of_multiple + 1)) // 2
        return sum_of_multiple
    print(sum_(3)+sum_(5)-sum_(15))
