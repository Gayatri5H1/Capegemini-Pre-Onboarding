n,x = map(int, input().split())
m = []
for _ in range(x):
    m.append(list(map(float, input().split())))
for st in zip(*m):
    print(sum(st)/x) 
