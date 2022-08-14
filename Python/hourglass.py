
def hourglassSum(arr):
    maxsum=-99 #for initialization
    
    for i in range(4):
        for j in range(4):
            # top value
            top=sum(arr[i][j:j+3])
            # mid value
            mid=arr[i+1][j+1]
            # bottom value
            bot=sum(arr[i+2][j:j+3])
            hourglass= top + mid + bot
            maxsum=max(hourglass,maxsum)

    return maxsum
# -----------------------------------------------------------------------
arr = []
for _ in range(6):
    arr.append(list(map(int, input("Enter elements: ").rstrip().split())))

print(hourglassSum(arr))

  