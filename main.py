from mygroupmates import groupmates

def One_student(student):
    print(
        student["name"].ljust(15),
        student["surname"].ljust(10),
        str(student["exams"]).ljust(30),
        str(student["marks"]).ljust(20)
    )

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10),
          u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        One_student(student)


print_students(groupmates)


def SortByMarks(students, Mark):
    for student in students:
        if (sum(student["marks"]) / len(student["marks"])) >= Mark:
            One_student(student)





Avg_Mark = float(input())

Sorted_Students = SortByMarks(groupmates, Avg_Mark)
