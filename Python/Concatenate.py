import numpy 
n,m,p = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
print(numpy.concatenate((a,b)))
