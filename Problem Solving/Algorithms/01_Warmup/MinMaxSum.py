arr=[1,3,5,7,9]
arr.sort()
# print(arr)
min=[]
for i in range(4):
    min.append(arr[i])
# print(min)
max=[]
for i in range(1,5):
    max.append(arr[i])
    
print(sum(min),end=" ")
print(sum(max))