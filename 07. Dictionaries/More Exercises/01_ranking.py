import operator


contest_dict = {}
users_dict = {}
user_points = {}

command = input()
while command != "end of contests":

    contest, password = command.split(":")

    contest_dict[contest] = password
    command = input()

line = input()
while line != "end of submissions":

    line = line.split("=>")
    contest_check = line[0]
    password_check = line[1]
    username = line[2]
    points = int(line[3])

    if contest_check in contest_dict and password_check == contest_dict[contest_check]:
        if username not in users_dict:
            users_dict[username] = {contest_check: points}
        else:
            if contest_check in users_dict[username]:
                if points > users_dict[username][contest_check]:
                    users_dict[username][contest_check] = points
            else:
                users_dict[username][contest_check] = points

    line = input()

#max points
for user, values in sorted(users_dict.items()):
    if user not in user_points:
        user_points[user] = 0
    for key, value in values.items():
        user_points[user] += value

maximum = max(user_points, key=user_points.get)

print(f"Best candidate is {maximum} with total {user_points[maximum]} points.")
# print(f"Best candidate is {max(user_points)} with total {max(user_points.values())} points.") - give max points with the latest user
print(f'Ranking:')

for keys, values in sorted(users_dict.items()):
    print(keys)
    # Dictionary in descending order by value
    for key, value in sorted(values.items(), key=operator.itemgetter(1), reverse=True):
        print(f'#  {key} -> {value}')
