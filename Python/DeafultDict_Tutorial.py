from collections import defaultdict
d = defaultdict(list)
n,m = map(int, input().split())
for i in range(1, n+1):
    w = input()
    d[w].append(i)
for _ in range(m):
    w = input()
    if w in d:
        print(*d[w])
    else:
        print(-1)
