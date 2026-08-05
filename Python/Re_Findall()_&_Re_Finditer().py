import re
s = input()
m = re.findall(r'(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])', s, re.I)
if m:
    print("\n".join(m))
else:
    print(-1)
