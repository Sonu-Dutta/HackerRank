from os import remove


if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))
    arr.sort()
    arr=set(arr)
    arr.remove(max(arr))
    print(max(arr))
    
    
  