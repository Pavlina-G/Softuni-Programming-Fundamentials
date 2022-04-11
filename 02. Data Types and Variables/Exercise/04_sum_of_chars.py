number = int(input())
sum = 0

for num in range(1, number + 1):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")