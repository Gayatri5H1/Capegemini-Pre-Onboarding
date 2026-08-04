import math
ab = int(input())
bc = int(input())
a = math.degrees(math.atan(ab/bc))
print(str(round(a)) + chr(176))
