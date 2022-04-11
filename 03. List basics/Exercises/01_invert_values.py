single_str = input() #input().split(" ")
my_list = single_str.split(" ")
new_list = []

for i in range(len(my_list)):
    new_list.append(-int(my_list[i]))

print(new_list)
