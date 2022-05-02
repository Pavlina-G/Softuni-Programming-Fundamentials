import re

mails = input()

user_pattern = r"( |^)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*"
host_pattern = r"[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

pattern = rf"{user_pattern}@{host_pattern}"
matches = re.finditer(pattern, mails)

for match in matches:
    print(match[0])