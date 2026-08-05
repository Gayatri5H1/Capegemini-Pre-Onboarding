from itertools import combinations
n = int(input())
l = input().split()
k = int(input())
cb = list(combinations(l,k))
ct = 0
for c in cb:
    if 'a' in c:
        ct += 1
print(ct/len(cb))
