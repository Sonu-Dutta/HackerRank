dic={}
s=list()
for _ in range(int(input("Enter number of students: "))):
    name = input(f"Enter name of student-{_+1}: ")
    score = float(input(f"Enter score of student-{_+1}: "))
    if score in dic:
        dic[score].append(name)
    else:
        dic[score]=[name]
    if score not in s:
        s.append(score)
m=min(s)
s.remove(m)
m1=min(s)
dic[m1].sort()
for i in dic[m1]:
    print(i)