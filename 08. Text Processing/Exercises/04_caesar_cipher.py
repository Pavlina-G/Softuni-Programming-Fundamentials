text = input()
new_text = ''

for i in text:
    new_text += chr(ord(i) + 3)
print(new_text)