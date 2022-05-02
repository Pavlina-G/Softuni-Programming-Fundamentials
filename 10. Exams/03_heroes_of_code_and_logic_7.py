n = int(input())
heroes_dict = {}

for i in range(n):
    line = input().split(' ')
    name = line[0]
    hit_points = int(line[1])
    mana_points = int(line[2])

    heroes_dict[name] = [hit_points, mana_points]

while True:
    command = input().split(' - ')

    if command[0] == "End":
        for key, value in heroes_dict.items():
            print(key)
            print(f"  HP: {value[0]}")
            print(f"  MP: {value[1]}")
        break

    hero_name = command[1]

    if command[0] == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]

        if heroes_dict[hero_name][1] - mp_needed >= 0:
            heroes_dict[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]

        heroes_dict[hero_name][0] -= damage
        if heroes_dict[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
        else:
            heroes_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command[0] == "Recharge":
        amount = int(command[2])
        if heroes_dict[hero_name][1] + amount > 200:
            amount = 200 - heroes_dict[hero_name][1]
            heroes_dict[hero_name][1] = 200
        else:
            heroes_dict[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == "Heal":
        amount = int(command[2])
        if heroes_dict[hero_name][0] + amount > 100:
            amount = 100 - heroes_dict[hero_name][0]
            heroes_dict[hero_name][0] = 100
        else:
            heroes_dict[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")


