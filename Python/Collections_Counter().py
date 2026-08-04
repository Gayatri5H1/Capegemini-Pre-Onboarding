# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
sz = list(map(int,input().split()))
sh = Counter(sz)
n = int(input())
m = 0
for _ in range(n):
    size, price = map(int, input().split())
    if sh[size] > 0:
        m += price
        sh[size] -= 1
print(m)
