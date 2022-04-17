names = input().split(", ")
sorted_list = sorted(names) # sorted alphabetically in ascending order
sorted_list = sorted(sorted_list, key=lambda x: -len(x)) # sorted by len of the name in descending order

print(sorted_list)
