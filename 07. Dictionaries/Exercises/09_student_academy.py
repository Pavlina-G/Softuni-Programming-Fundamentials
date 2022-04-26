num = int(input())
grades_info = {}
average_grade = {}

for i in range(num):
    student = input()
    grade = float(input())

    if student not in grades_info:
        grades_info[student] = []
    grades_info[student] += [grade]

for name, grades in grades_info.items():
    average_grade[name] = sum(grades) / len(grades)
    if average_grade[name] >= 4.50:
        print(f"{name} -> {average_grade[name]:.2f}")
