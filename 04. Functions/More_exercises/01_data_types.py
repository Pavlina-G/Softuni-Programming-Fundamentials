def data_types(type_num, num):
    if type_num == "int":
        return int(num) * 2
    elif type_num == "real":
        result = float(num) * 1.5
        return f"{result:.2f}"
    else:
        return "$" + num + "$"


type_of_string = input()
data = input()
print(data_types(type_of_string, data))
