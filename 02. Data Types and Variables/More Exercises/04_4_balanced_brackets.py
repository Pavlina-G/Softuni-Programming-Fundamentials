lines = int(input())
my_string = ""

for i in range(lines):
    input_str = input()
    my_string = my_string + input_str

condition = False
counter = 0

for char in my_string:
    # if char == ")" and counter % 2 == 0:
    #     break
    if char == "(":
        counter += 1
    if counter % 2 != 0 and char == ")":
        condition = True

if condition:
    print("BALANCED")
else:
    print("UNBALANCED")

