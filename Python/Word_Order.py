from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    w = input()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
print(len(d))
print(*d.values())
