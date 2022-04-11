number_of_people_P = int(input())
capacity_of_elevator_N = int(input())

elevator_courses = number_of_people_P // capacity_of_elevator_N
additional_course = number_of_people_P % capacity_of_elevator_N

if 0 < additional_course < capacity_of_elevator_N:
    elevator_courses += 1

print(elevator_courses)