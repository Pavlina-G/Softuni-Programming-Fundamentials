list_numbers = [int(num) for num in input().split(", ")]  # [1, 2, 3, 4, 5]
beggar_count = int(input())
sum_list = [0] * beggar_count  # if beggars = 2 # [0, 0]
count = 0

for i in range(len(list_numbers)):

    sum_list[count] += list_numbers[i]
    count += 1

    if count >= beggar_count:
        count = 0

print(sum_list)

#Second:
list_numbers = list(map(int, (input().split(", "))))
count_beggars = int(input())
sum_list = [0] * count_beggars
counter = 0

for i in range(len(list_numbers)):
    sum_list[counter] += list_numbers[i]
    counter += 1

    if counter >= count_beggars:
        counter = 0

print(sum_list)



