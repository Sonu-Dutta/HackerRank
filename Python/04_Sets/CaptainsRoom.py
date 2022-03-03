lst=list(map(int,input().split()))
s1=set()
s2=set()
for i in lst:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
print(s1)
print(s2)
s=s1.difference(s2)
print(*s)