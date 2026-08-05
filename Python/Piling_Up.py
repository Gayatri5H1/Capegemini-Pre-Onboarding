from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    c = deque(map(int, input().split()))
    l = float('inf')
    p = True
    while c:
        if c[0] >= c[-1]:
            cu = c.popleft()
        else:
            cu = c.pop() 
        if cu <= l:
            l = cu
        else:
            p = False
            break
    print("Yes" if p else "No")
