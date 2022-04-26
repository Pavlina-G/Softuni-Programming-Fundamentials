command = input()
course_dict = {}

while command != 'end':
    command = command.split(" : ")
    course = command[0]
    name = command[1]

    if course not in course_dict:
        course_dict[course] = [name]
    else:
        course_dict[course] += [name]

    command = input()

for course, names in course_dict.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")