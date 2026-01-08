#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    i, j = 0, k
    max_prod = 0
    while j <= n:
        prod = 1
        digits = list(map(int, [*num[i:j]]))
        for x in digits:
            prod *= x
        max_prod = max(max_prod, prod)
        i += 1
        j += 1
    print(max_prod)