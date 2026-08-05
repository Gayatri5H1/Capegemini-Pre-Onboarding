a = set(map(int, input().split()))
n = int(input())
res = True
for _ in range(n):
    b = set(map(int, input().split()))
    if not a.issuperset(b) or a==b:
        res = False
print(res) 
