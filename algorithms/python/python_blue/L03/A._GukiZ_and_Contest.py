class Student:
    def __init__(self, rating, id):
        self.rating = rating
        self.id = id

n = int(input())
a = list(map(int, input().split()))

student = []
for i in range(n):
    student.append(Student(a[i], i))
        
student.sort(reverse = True, key = lambda Student: Student.rating)

p = 1
pos = [0] * 2001
pos[student[0].id] = 1
for i in range(1, n):
    if student[i].rating == student[i - 1].rating:
        pos[student[i].id] = p
    else:
        p = i + 1
        pos[student[i].id] = p        

for i in range(n):
    print(pos[i], end = " ")
