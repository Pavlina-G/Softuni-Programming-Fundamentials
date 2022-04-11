n = int(input())
list = []

for i in range(n):
    current_number = int(input())
    list.append(current_number)

command = input()
filtered_list = []

if command ==  "even":
    for num in list:
        if num % 2 == 0:
            filtered_list.append(num)
elif command == "odd":
    for num in list:
        if num % 2 != 0:
            filtered_list.append(num)
elif command == "negative":
    for num in list:
        if num < 0:
            filtered_list.append(num)
elif command == "positive":
    for num in list:
        if num >= 0:
            filtered_list.append(num)

print(filtered_list)
