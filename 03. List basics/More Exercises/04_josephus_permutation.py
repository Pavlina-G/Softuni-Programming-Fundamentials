number_people = list(map(int, input().split(' ')))
number_k = int(input())
order_of_execution = []
counter = 0

index = 0
while number_people:
    counter += 1
    if counter % number_k == 0:
        order_of_execution.append(number_people[index])
        number_people.pop(index)
    else:
        index += 1
    if index >= len(number_people):
        index = 0

print(str(order_of_execution).replace(" ", ""))
