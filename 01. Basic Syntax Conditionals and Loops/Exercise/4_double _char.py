string = input()
new_string = ""

for value in string:
    for new_value in value:
        new_value += value
        print(new_value, end = "")
