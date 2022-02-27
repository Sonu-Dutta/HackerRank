def chocolateFeast(n, c, m):
    choco=n//c
    wraps=choco
    while wraps>=m:
        choco+=wraps//m
        wraps=wraps//m +wraps%m
    return choco

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        print(chocolateFeast(n, c, m))

  
