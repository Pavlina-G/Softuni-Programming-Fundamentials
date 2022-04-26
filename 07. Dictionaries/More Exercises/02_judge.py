def judge():
    contests_dict = {}
    users_dict = {}

    while True:
        command = input()

        if command == 'no more time':
            break

        info = command.split(' -> ')
        username = info[0]
        contest = info[1]
        points = int(info[2])

        if contest not in contests_dict:
            contests_dict[contest]= {username: points}
            contests_dict[contest][username] = points
        else:
            if username not in contests_dict[contest]:
                contests_dict[contest][username] = points
            else:
                if points > contests_dict[contest][username]:
                    contests_dict[contest][username] = points

            # print(contests_dict) # {'Algo': {'Peter': 400}}
            # print(contests_dict[contest]) # {'Peter': 400}
            # print(contests_dict[contest][username]) # 400

    for keys, values in contests_dict.items():
        for user, point in values.items():
            if user not in users_dict:
                users_dict[user] = point
            else:
                users_dict[user] += point
    print(users_dict)

    for contest, values in contests_dict.items():
        counter = 0
        print(f'{contest}: {len(contests_dict[contest])} participants')

        for user, point in sorted(values.items(), key=lambda x: (-x[1], x[0])):
            counter += 1
            print(f'{counter}. {user} <::> {point}')

    print('Individual standings:')
    counter = 0

    for user, point in sorted(users_dict.items(), key=lambda x: (-x[1], x[0])):
        counter += 1
        print(f'{counter}. {user} -> {point}')


judge()


