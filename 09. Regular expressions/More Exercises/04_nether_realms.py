import re

char_regex = r"[^0-9+\+\-\*\/\.]"
numbers_regex = r"[+|-]?\d+\.?\d*"

names = sorted(re.split(", *", input()))
demons = {}

for demon in names:
    demon = demon.strip()
    characters = []
    numbers = []
    demons[demon] = []
    health = 0
    damage = 0

    characters.extend(re.findall(char_regex, demon))
    numbers.extend(list(map(float, re.findall(numbers_regex, demon))))

    multiply = demon.count('*')
    divide = demon.count('/')

    for char in characters:
        health += ord(char)

    damage = sum(numbers)
    for i in range(multiply):
        damage *= 2
    for i in range(divide):
        damage /= 2

    demons[demon].append(health)
    demons[demon].append(damage)

for key, value in sorted(demons.items(), key=lambda x: x):
    print(f'{key} - {value[0]} health, {value[1]:.2f} damage')


