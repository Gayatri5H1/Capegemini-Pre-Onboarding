import re
import email.utils
p = r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$'
for _ in range(int(input())):
    n,a = email.utils.parseaddr(input())
    if re.match(p,a):
        print(email.utils.formataddr((n,a)))
