import re
n = int(input())  
for _ in range(n):
    l = input()
    l = re.sub(r'(?<= )&&(?= )', 'and', l)
    l = re.sub(r'(?<= )\|\|(?= )', 'or', l)
    print(l)
