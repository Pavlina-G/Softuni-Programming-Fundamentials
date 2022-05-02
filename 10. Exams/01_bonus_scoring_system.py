from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
condition = False

for student in range(students):
    total_bonus = 0
    attendance = int(input())
    if lectures != 0:
        total_bonus = (attendance / lectures) * (5 + bonus)
        if total_bonus > max_bonus:
            max_bonus = total_bonus
            output = attendance
            condition = True
    else:
        break
if not condition:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")
else:
    print(f"Max Bonus: {ceil(max_bonus)}.")
    print(f"The student has attended {output} lectures.")