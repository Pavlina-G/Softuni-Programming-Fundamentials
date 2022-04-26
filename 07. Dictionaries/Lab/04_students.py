command = input()
students_dict = {}

while ":" in command:
    info = command.split(":") # create tuple (name, id, course) = command.split(":")
    name = info[0]
    id = int(info[1])
    course = info[2]

    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name

    command = input()

course_type = command
if "_" in course_type:
    course_type = course_type.replace("_", " ")

# for key, value in students_dict.items():
#     if key == course_type:
#         for id, name in value.items():
#             print(f"{name} - {id}")

for i in students_dict[course_type]:
    print(f"{students_dict[course_type][i]} - {i}")


