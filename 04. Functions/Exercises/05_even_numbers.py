# even_numbers = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))
# print(even_numbers)

def even_numbers(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
    print(even_list)


numbers = list(map(int, input().split(" ")))
even_numbers(numbers)
