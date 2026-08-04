from collections import namedtuple
n = int(input())
st = namedtuple('Student', input().split())
t = 0
for _ in range(n):
    student = st(*input().split())
    t += int(student.MARKS)
print(t/n)
