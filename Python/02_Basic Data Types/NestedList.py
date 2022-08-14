if __name__ == '__main__':
    a=[]
    b=[]
    n=int(input("Enter number of students: "))
    for _ in range(n):
        name = input(f"Enter name of student-{_+1}: ")
        score = float(input(f"Enter score of student-{_+1}: "))
        a.append(name)
        b.append(score)
    print(a)
    print(b)
    dic={a[i]:b[i] for i in range(len(a))}
    print(dic)
    
    b.sort()
    
            