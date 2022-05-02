import re

regex = r"(www\.)([a-zA-Z]*\d*-*)+(\.[a-z]+){1,}"

while True:
    text = input()
    if not text:
        break
    matches = re.search(regex, text)
    if matches is not None:
        print(matches[0])


