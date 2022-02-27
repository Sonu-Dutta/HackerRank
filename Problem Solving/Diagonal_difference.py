# Diagonal Difference

def diagonalDifference(arr):
    leftDi = rightDi=0
    for i in range(n):
        leftDi+=arr[i][i]
        rightDi+=arr[i][n-1-i]
    return abs(leftDi-rightDi)

# --------------------------------------------------------------------
n = int(input("Enter length of array: "))
arr = []
for _ in range(n):
    arr.append(list(map(int, input("Enter elements: ").split())))
print(diagonalDifference(arr)) 
