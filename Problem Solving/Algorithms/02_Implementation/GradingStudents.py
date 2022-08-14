def gradingStudents(grades):
    r=[]
    for g in grades:
        if g>=38:
            m=g%5             
            if m>=3:
                g+=(5-m)
        r.append(g)
    return r
if __name__ == '__main__':
    grades_count = int(input("Enter total grades: ").strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input("Enter grades: ").strip())
        grades.append(grades_item)

print(gradingStudents(grades))
