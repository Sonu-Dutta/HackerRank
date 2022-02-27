# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

# Sample Input 0
# 3
# Sample Output 0
# Weird

# Sample Input 1
# 24
# Sample Output 1
# Not Weird

if __name__ == '__main__':
    n = int(input("Enter a number: ").strip())
    if n%2!=0:
        print("Weird")
    elif (n%2==0 and (n in range(2,6))):
        print("Not Weird")
    elif(n%2==0 and (n in range(6,21))):
        print("Weird")
    elif(n%2==0 and (n>20)):
        print("Not Weird")