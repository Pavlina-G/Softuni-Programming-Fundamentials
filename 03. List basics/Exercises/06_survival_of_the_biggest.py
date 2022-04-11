list_of_numbers = [int(num) for num in input().split(" ")]
removal_number = int(input())

for i in range(removal_number):
    list_of_numbers.remove(min(list_of_numbers))

print(*list_of_numbers, sep = ", ")
# from list [10, 9, 8] prints # 10, 9, 8
