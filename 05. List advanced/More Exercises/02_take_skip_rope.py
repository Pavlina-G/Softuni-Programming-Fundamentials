string = input()
number_list = []
text_list = []
result_list = []

for i, value in enumerate(string):
    if str(value).isdigit():
        number_list.append(value)
    else:
        text_list.append(value)

take_list = [int(number_list[x]) for x in range(len(number_list)) if int(x) % 2 == 0]
skip_list = [int(number_list[x]) for x in range(len(number_list)) if int(x) % 2 != 0]

result_list = []

while len(skip_list) > 0:

    if len(take_list) > 0:
        add_index = take_list[0]
        result_list += text_list[:add_index]
        take_list.pop(0)
    if len(skip_list) > 0:
        skip_index = skip_list[0]
        del text_list[:add_index+skip_list[0]]
        skip_list.pop(0)

print("".join(result_list))



