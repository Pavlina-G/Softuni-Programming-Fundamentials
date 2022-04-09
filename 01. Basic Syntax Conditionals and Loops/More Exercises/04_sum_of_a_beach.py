text = input()
text = text.lower()
counter = 0

list = ["sand", "water", "fish", "sun"]

for item in list:
    if item in text: # if sand, water, fish, sun in text
        word_found_counter = text.count(item)
        counter += word_found_counter
print(counter)

# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x) #hello, and welcome to my world!