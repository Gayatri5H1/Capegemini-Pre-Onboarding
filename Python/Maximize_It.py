from itertools import product
k,m = map(int, input().split())
l = []
for _ in range(k):
    l.append(list(map(int, input().split()))[1:])
ans = 0
for p in product(*l):
    ans = max(ans, sum(x*x for x in p)%m)
print(ans)
