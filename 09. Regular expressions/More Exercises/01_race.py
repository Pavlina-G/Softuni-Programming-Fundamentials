import re

names = input().split(', ')
racers_dict = {}

for name in names:
    if name not in racers_dict:
        racers_dict[name] = 0

regex_name = r"[a-z]*[A-Z]*"
regex_distance = r"\d"

while True:
    line = input()

    if line == 'end of race':
        break

    racer = re.findall(regex_name, line)
    distance = re.findall(regex_distance, line)
    if len(racer) > 0 and ''.join(racer) in names:
        if len(regex_distance) > 0:
            racers_dict[''.join(racer)] += sum(map(int, distance))

sorted_dict = dict(sorted(racers_dict.items(), key=lambda x: -x[1]))

print(f"1st place: {[key for key in sorted_dict.keys()][0]}")
print(f"2nd place: {[key for key in sorted_dict.keys()][1]}")
print(f"3rd place: {[key for key in sorted_dict.keys()][2]}")
