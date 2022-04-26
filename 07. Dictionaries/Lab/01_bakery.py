food = input().split(" ")
food_dict = {} # food_dict = dict()

for i in range(0, len(food), 2):
    key = food[i]
    value = food[i + 1]
    food_dict[key] = int(value)

print(food_dict)
