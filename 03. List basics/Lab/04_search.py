number = int(input())
word = input()
list_of_string = []

for i in range(number):
    current_string = input()
    list_of_string.append(current_string)

print(list_of_string)

for element in list_of_string[::-1]:
    # print(element)
    if word not in element:
        list_of_string.remove(element)

print(list_of_string)




