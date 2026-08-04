m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
for i in sorted(a^b):
    print(i)
