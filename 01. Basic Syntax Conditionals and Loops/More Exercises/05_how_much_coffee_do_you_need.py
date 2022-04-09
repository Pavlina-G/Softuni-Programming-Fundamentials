command = input()

events = ["coding", "dog", "cat", "movie"]
coffee = 0

while command != "END":

    if command.islower() and command in events:
        coffee += 1
    elif command.isupper() and command.casefold() in events:
        coffee += 2
    else:
        pass
    command = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)



