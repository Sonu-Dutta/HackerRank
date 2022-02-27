def Opertions():
    global output
    ol=input().split()
    operation=ol[0]
    uSet=set(map(int,input().split()))
    if operation=="intersection_update":
        a.intersection_update(uSet)
    elif operation=="symmetric_difference_update":
        a.symmetric_difference_update(uSet)
    elif operation=="difference_update":
        a.difference_update(uSet)
    output=sum(a)

input()
a=set(map(int,input().split()))
n=int(input())
for i in range(n):
    Opertions()
print(output)
    