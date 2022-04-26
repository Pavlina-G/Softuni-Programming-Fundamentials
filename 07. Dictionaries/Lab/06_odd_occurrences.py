elements = input().split(" ")
elements_dict = dict()

for element in elements:
    element = element.lower()
    if element not in elements_dict:
    #     elements_dict[element] = 1
    # else:
    #     elements_dict[element] += 1
        elements_dict[element] = 0
    elements_dict[element] += 1

for (key, value) in elements_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
