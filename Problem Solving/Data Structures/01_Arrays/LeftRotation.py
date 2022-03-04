def rotateLeft(d, arr):
    # out = list(arr)
    # a_len = len(arr)
    # for ind, el in enumerate(arr):
    #     # print(ind,el)
    #     out[(ind + a_len - d) % a_len] = el
    # return out
    arr=arr[d:]+arr[:d]
    # return(arr)
    print(*arr)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result=rotateLeft(d, arr)

   