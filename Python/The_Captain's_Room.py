k = int(input())
r = list(map(int, input().split()))
print((sum(set(r))*k-sum(r))//(k-1))
