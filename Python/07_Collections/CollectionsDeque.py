from collections import deque
d = deque()
for _ in range(int(input())):
    lst=list(input().split())
    if lst[0]=='append':
        d.append(int(lst[1]))
    elif lst[0]=='appendleft':
        d.appendleft(int(lst[1]))
    elif lst[0]=='popleft':
        d.popleft()
    elif lst[0]=='pop':
        d.pop()
    
for i in d:
    print(i, end=" ")