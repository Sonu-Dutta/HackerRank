# You are given two sets, A and B .
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Input Format

# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.



t=int(input("Enter number of test cases: "))
for i in range(t):
    a=input("Enter length of set A: ")
    A=set(input("Enter elements of set A: ").split())
    b=input("Enter length of set B: ")
    B=set(input("Enter elements of set B: ").split())
    print(A.issubset(B))