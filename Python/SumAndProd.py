import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
# print(numpy.sum(A, axis=0))
print(numpy.prod(numpy.sum(A, axis=0), axis=0))