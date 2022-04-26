characters = input().split(", ")
# ascii_dict = {}

# for char in characters:
#     ascii_dict[char] = ord(char)

ascii_dict = {char: ord(char) for char in characters}
print(ascii_dict)