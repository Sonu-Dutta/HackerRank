
def countApplesAndOranges(s, t, a, b, apples, oranges):
    TApples=TOranges=0
    for i in range(len(apples)):
        if s<= a+apples[i] <=t:
            TApples+=1
    for i in range(len(oranges)):
        if s<= b+oranges[i] <=t:
            TOranges+=1      
    print(TApples) 
    print(TOranges)
            

if __name__ == '__main__':
    first_multiple_input = input("Enter s and t: ").rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input("Enter a and b: ").rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input("Enter m and n: ").rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input("Apples: ").rstrip().split()))

    oranges = list(map(int, input("Oranges: ").rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
