def average(array):
    
    return sum(set(array))/len(set(array))
# print(average([2,3,4,5]))
print(average( list(map(int, input().split()))))