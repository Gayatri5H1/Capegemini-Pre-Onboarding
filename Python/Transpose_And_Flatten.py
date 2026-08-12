import numpy
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
a = numpy.array(a)
print(numpy.transpose(a))
print(a.flatten())
