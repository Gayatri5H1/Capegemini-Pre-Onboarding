from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    c = input().split()
    if c[0] == "append":
        d.append(c[1])
    elif c[0] == "appendleft":
        d.appendleft(c[1])
    elif c[0] == "pop":
        d.pop()
    elif c[0] == "popleft":
        d.popleft()
print(*d)
