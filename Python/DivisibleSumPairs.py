
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i]+ar[j])%k==0:
                count+=1
    return count

if __name__ == '__main__':
 

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    print(divisibleSumPairs(n, k, ar))