total_rows=int(input("Enter no of rows: "))
for row in range(1,total_rows+1):
    for space in range(1,(total_rows-row)+1):
        print(" ",end="")
    for symbol in range(1,row+1):
        print("#",end="")
    print()