n = int(input())
a = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    op, len = input().split()
    b = set(map(int, input().split()))
    if op == "intersection_update":
        a.intersection_update(b)
    elif op == "update":
        a.update(b)
    elif op == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    elif op == "difference_update":
        a.difference_update(b)
print(sum(a))
