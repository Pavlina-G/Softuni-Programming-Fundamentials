import re
text = input()

print(len(re.findall(r"sand|water|fish|sun", text, flags=re.IGNORECASE)))
