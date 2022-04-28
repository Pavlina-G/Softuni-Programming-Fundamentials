text = input()
new_text = ''
explosions = 0

for i in range(len(text)):
    if text[i] == '>':
        explosions += int(text[i+1])
        new_text += text[i]
    elif text[i] != '>' and explosions > 0:
        explosions -= 1
    else:
        new_text += text[i]

print(new_text)


