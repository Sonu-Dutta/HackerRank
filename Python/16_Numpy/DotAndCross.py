import numpy
n=int(input())
a = numpy.array([input().split() for _ in range(n)],int)
b = numpy.array([input().split() for _ in range(n)],int)
# print(a)
# print(b)
m = numpy.dot(a,b)
# l=numpy.cross(a,b)
print (m)
# print(l)