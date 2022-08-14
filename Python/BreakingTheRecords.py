
def breakingRecords(scores):
    minc=maxc=0
    mins=maxs=scores[0]
    
    for i in range(1,len(scores)):
        if mins<scores[i]:
            mins=scores[i]
            minc+=1
        elif maxs>scores[i]:
            maxs=scores[i]
            maxc+=1
    return minc,maxc  

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    print(breakingRecords(scores))

