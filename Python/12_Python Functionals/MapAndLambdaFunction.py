cube = lambda x: x**3

def fibonacci(n):
    if n<2:
        return range(n)
    init = [0,1]
    for i in range(0,n-2):
            add =init[i+1]+init[i]
            init.append(add)
    return(init)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))