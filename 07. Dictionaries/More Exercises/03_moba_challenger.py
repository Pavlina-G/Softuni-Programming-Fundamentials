def position_skills(player, position, skill, positions):
    if player not in positions:
        positions[player] = {position: skill}
        positions[player][position] = skill
    else:
        if position not in positions[player]:
            positions[player].update({position: skill})
        else:
            if skill > positions[player][position]:
                positions[player][position] = skill
    return positions


def moba_challenger():
    positions = {}
    total_skills = {}

    while True:
        command = input()
        if command == "Season end":
            break

        if '->' in command:
            info = command.split(' -> ')
            player = info[0]
            position = info[1]
            skill = int(info[2])

            positions = position_skills(player, position, skill, positions)

        elif ' vs ' in command:
            info = command.split(' vs ')
            player1 = info[0]
            player2 = info[1]
            duel = False

            # positions = duel(player1, player2, positions)
            if player1 in positions and player2 in positions:
                for p1 in positions[player1]:
                    for p2 in positions[player2]:

                        if p1 == p2:
                            duel = True
                            if positions[player1][p1] > positions[player2][p2]:
                                positions.pop(player2)
                                break
                            elif positions[player1][p1] < positions[player2][p2]:
                                positions.pop(player1)
                                break
                            else:
                                break
                    if duel:
                        break


    for user, values in positions.items():
        for key, skill in values.items():
            if user not in total_skills:
                total_skills[user] = skill
            else:
                total_skills[user] += skill

    for user, skill in sorted(total_skills.items(), key=lambda x: (-x[1], x[0])):
        print(f'{user}: {skill} skill')
        for keys, values in positions.items():
            if keys == user:
                for position, point in sorted(values.items(), key=lambda x: (-x[1], x[0])):
                    print(f'- {position} <::> {point}')


moba_challenger()