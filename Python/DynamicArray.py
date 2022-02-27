def dynamicArray(n, queries):
    seq=[[]for _ in range(n)]
    lastAns=0
    result=[]
    
    for q,x,y in queries:
        if q==1:
            idx=(x^lastAns)%n
            seq[idx].append(y)
            
        else:
            idx=(x^lastAns)%n
            v=y%len(seq[idx])
            lastAns=seq[idx][v]
            result.append(lastAns)
    return result
            

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)