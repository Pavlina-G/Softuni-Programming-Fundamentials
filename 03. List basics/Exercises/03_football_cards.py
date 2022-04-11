card = input().split(" ")
team_a_counter = 11
team_b_counter = 11

terminated = False

new_list = list(set(card)) # set ignores duplicates players number

for i in range(1,11 + 1):
    team_a_counter -= int(new_list.count(f"A-{i}"))
    team_b_counter -= int(new_list.count(f"B-{i}"))

    if team_a_counter < 7 or team_b_counter < 7:
        print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")
        print(f"Game was terminated")
        terminated = True
        break

if not terminated:
    print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")


