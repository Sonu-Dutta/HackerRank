n, x = map(int, input().split()) 
sheet = []
for _ in range(x):
    sheet.append(list(map(float, input().split()) ))
# print(sheet)
for i in zip(*sheet): 
    # print(i)
    print( sum(i)/len(i))