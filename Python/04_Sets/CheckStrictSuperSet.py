A=set(map(int,input("Enter elements of set A:").split()))
n=int(input("Enter number of test cases: "))
val=""
for i in range(n):
    B=set(map(int,input("Enter elements of set B:").split()))
    if len(B.difference(A))==0:
        val="True"
    else:
        val="False"
        break
print(val)