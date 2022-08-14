# a,b = [set(input().split()) for _ in range(4)][1::2]
# print('\n'.join(sorted(a^b, key=int)))

from ntpath import join


a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print('\n'.join(sorted(r,key=int)))