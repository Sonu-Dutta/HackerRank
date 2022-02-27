def migratoryBirds(arr):
    l=[0]*count
    
    for i in arr:
        l[i]+=1
    return l.index(max(l))

if __name__ == '__main__':

    count = int(input("Enter size of array: ").strip())

    arr = list(map(int, input("Enter values: ").rstrip().split()))

    print(migratoryBirds(arr))