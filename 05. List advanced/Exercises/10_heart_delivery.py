def jumps(num):
    if text[num] == 0:
        print(f"Place {num} already had Valentine's day.")
    else:
        text[num] -= 2
        if text[num] == 0:
            print(f"Place {num} has Valentine's day.")

text = list(map(int, input().split("@")))
start_position = 0
current_position = 0
while True:

    command = input()
    if command == "Love!":
        break

    info = command.split(" ")
    jump = int(info[1])

    current_position += jump
    if current_position in range(len(text)):
        jumps(current_position)
    else:
        current_position = start_position
        jumps(current_position)
last_position = current_position

print(f"Cupid's last position was {last_position}.")
if sum(text) == 0:
    print("Mission was successful.")
else:
    left_house = len(text) - text.count(0)
    print(f"Cupid has failed {left_house} places.")

