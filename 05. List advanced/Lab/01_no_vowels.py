text = input()
vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
text = [x for x in text if x not in vowels]
print("".join(text))
