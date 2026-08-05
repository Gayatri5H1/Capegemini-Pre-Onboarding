n = int(input())
num = input().split()
print(all(int(x)> 0 for x in num) and any(x == x[::-1] for x in num))
