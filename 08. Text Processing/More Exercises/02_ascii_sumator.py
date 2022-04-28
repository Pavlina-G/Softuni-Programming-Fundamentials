start_char = ord(input())
end_char = ord(input())
text = input()
searched_text = ''
sum = 0
for i in range(start_char + 1, end_char):
    searched_text += chr(i)

for ch in text:
    if ch in searched_text:
        sum += ord(ch)
print(sum)