heroes_dict = {}

while True:
    command = input()
    if command == "End":
        break

    info = command.split(' ')
    name = info[1]
    if info[0] == "Enroll":
        if name not in heroes_dict:
            heroes_dict[name] = []
        else:
            print(f"{name} is already enrolled.")

    elif info[0] == "Learn":
        spell_name = info[2]
        if name not in heroes_dict:
            print(f"{name} doesn't exist.")
        else:
            if spell_name not in heroes_dict[name]:
                heroes_dict[name].append(spell_name)
            else:
                print(f"{name} has already learnt {spell_name}.")

    elif info[0] == "Unlearn":
        spell_name = info[2]
        if name not in heroes_dict:
            print(f"{name} doesn't exist.")
        else:
            if spell_name not in heroes_dict[name]:
                print(f"{name} doesn't know {spell_name}.")
            else:
                heroes_dict[name].remove(spell_name)

print("Heroes:")
for hero, spell_names in heroes_dict.items():
    if len(spell_names) > 0:
        print(f"== {hero}: {', '.join(spell_names)}")
    else:
        print(f"== {hero}:")
