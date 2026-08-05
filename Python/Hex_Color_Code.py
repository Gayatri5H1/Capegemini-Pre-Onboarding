import re 
n = int(input()) 
ins = False
for _ in range(n):
    l = input()
    if '{' in l:
        ins = True
    if '}' in l:
        ins = False
    if ins:
        ms = re.findall(r'(?i)(?<=[: ,])#(?:[0-9a-f]{3}|[0-9a-f]{6})\b', l)
        for m in ms:
            print(m)
