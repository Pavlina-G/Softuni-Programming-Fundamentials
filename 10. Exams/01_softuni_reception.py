first_emp = int(input())
second_emp = int(input())
third_emp = int(input())
efficiency = [first_emp, second_emp, third_emp]
students_count = int(input())
hours = 0

while students_count > 0:
    students_count -= sum(efficiency)
    hours += 1

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")