key = int(input())
lines = int(input())

message = ""

for i in range(1, lines + 1):
    letter = input()
    current_letter = ord(letter) + key
    message += chr(current_letter)
    current_letter = 0

print(message)
