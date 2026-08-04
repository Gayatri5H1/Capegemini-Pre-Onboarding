from collections import OrderedDict
d = OrderedDict()
n = int(input())
for _ in range(n):
    item = input().rsplit(" ",1)
    name = item[0]
    price = int(item[1])
    if name in d:
        d[name] += price
    else:
        d[name] = price
for name, price in d.items():
    print(name, price)
