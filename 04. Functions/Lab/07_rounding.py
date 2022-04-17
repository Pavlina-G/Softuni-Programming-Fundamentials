def rounding(base_list):
    new_list = []
    for num in base_list:
        new_list.append(round(num))
    return new_list


number_list = list(map(float, input().split(" ")))
print(rounding(number_list))
