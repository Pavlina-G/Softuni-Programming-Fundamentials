searched_text = input()
text = input()

while searched_text in text:
    text = text.replace(searched_text, '')

print(text)