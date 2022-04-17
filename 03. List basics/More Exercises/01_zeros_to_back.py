single_string = list(map(int, input().split(', ')))
zero_list = []

for i in single_string[::-1]:
    if i == 0:
        zero_list.append(i)
        single_string.remove(0)

single_string = single_string + zero_list
print(single_string)

