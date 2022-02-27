import numpy as np

n, m = [int(x) for x in input().strip().split()]
array = np.array([[int(x) for x in input().strip().split()] for _ in range(n)], dtype = float)
print(np.mean(array, axis = 1))
print(np.var(array, axis = 0))
st=np.std(array)
print(round(st,11))
# print("{:.11f}".format(st))