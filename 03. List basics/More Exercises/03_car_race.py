numbers = list(map(int, input().split(" ")))
first_car = numbers[:len(numbers)//2]

reversed_list = numbers[::-1]
second_car = reversed_list[:len(numbers)//2]

left = False
sum1 = 0
sum2 = 0

for value1, value2 in zip(first_car, second_car):
    sum1 += value1
    if value1 == 0:
        sum1 *= 0.8
    sum2 += value2
    if value2 == 0:
        sum2 *= 0.8

if sum1 <= sum2:
    left = True

if left:
    print(f"The winner is left with total time: {sum1:.1f}")
else:
    print(f"The winner is right with total time: {sum2:.1f}")


