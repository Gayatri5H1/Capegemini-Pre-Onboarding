import re
s = input()  
k = input()
ms = list(re.finditer(r'(?={})'.format(re.escape(k)), s))
if ms:
    for m in ms:
        print((m.start(), m.start() + len(k)-1))
else:
    print((-1,-1))
