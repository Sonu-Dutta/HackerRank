import numpy
# print(numpy.identity(3))
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0')) 