import re

n = int(input())
key_letters = r"S|T|A|R"
regex = r'(?<=@)(?P<planet>[A-Z][a-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)[^\@\-\!\:\>]*(?P<attack>!A!|!D!)[^\@\-\!\:\>]*->(?P<soldiers>\d+)'

# planet_name = r"(?<=@)[a-zA-Z]+"
# population = r"(?<=:)\d+"
# attack_type = r"(?<=!)A|D(?=!)"
# soldiers = r"(?<=->)\d+"
attacked_planet = []
destroyed_planet = []

for i in range(n):
    line = input()
    new_line = ''

    key = len(re.findall(key_letters, line, re.IGNORECASE))
    for symbol in line:
        new_line += chr(ord(symbol) - key)

    matches = re.finditer(regex, new_line)

    for match in matches:
        planet = match.group('planet')
        attack = match.group('attack')

        if attack == '!A!':
            attacked_planet.append(planet)
        elif attack == '!D!':
            destroyed_planet.append(planet)

print(f"Attacked planets: {len(attacked_planet)}")
if len(attacked_planet) > 0:
    for planet in sorted(attacked_planet):
        print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planet)}")
if len(destroyed_planet) > 0:
    for planet in sorted(destroyed_planet):
        print(f"-> {planet}")
