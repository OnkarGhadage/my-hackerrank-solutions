# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())

orders = OrderedDict()

for i in range(N):
    order = input().split()
    price = int(order[-1])
    order.remove(order[-1])
    item_name = " ".join(order)
    if item_name in orders:
        orders[item_name] += price
    else:
        orders[item_name] = price

for item, net_price in orders.items():
    print(item, net_price)
