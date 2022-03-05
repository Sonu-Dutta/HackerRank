numnodes = int(input())
colors = [int(x)*2-1 for x in input().split()]

edges = [list() for _ in range(numnodes+1)]
for _ in range(numnodes-1):
    a,b = [int(x) for x in input().split()]
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

# calculate the minimum and maximum possible weights
# for a subtree rooted at each node
parents = [-1] * numnodes
minima = list(colors)
maxima = list(colors)
children_done = [False] * numnodes
todo = [0,0]
while todo:
    node = todo.pop()
    if not children_done[node]:
        for child in edges[node]:
            if child != parents[node]:
                parents[child] = node
                todo.append(child)
                todo.append(child)
        children_done[node] = True
    else:
        for child in edges[node]:
            if child != parents[node]:
                minima[node] += minima[child]
                maxima[node] += maxima[child]
        if minima[node] > 0:
            minima[node] = 0
        if maxima[node] < 0:
            maxima[node] = 0
        
# find the node with the best subtree
best = 0
bestroot = 0
for i in range(numnodes):
    if best < 0 - minima[i]:
        best = 0 - minima[i]
        bestroot = i
    if best < maxima[i]:
        best = maxima[i]
        bestroot = i

# find the nodes in the best subtree
subtree = []
todo = [bestroot]
if 0-minima[bestroot] > maxima[bestroot]:
    while todo:
        node = todo.pop()
        if minima[node] < 0:
            subtree.append(node+1)
            for child in edges[node]:
                if child != parents[node]:
                    todo.append(child)
else:
    while todo:
        node = todo.pop()
        if maxima[node] > 0:
            subtree.append(node+1)
            for child in edges[node]:
                if child != parents[node]:
                    todo.append(child)

subtree.sort()

# print the result
print(best)
print(len(subtree))
print(*subtree)