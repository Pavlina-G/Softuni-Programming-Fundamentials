def even_odd_sum(nums):
    even_sum = []
    odd_sum = []
    for i in nums:
        if i % 2 == 0:
            even_sum.append(i)
        else:
            odd_sum.append(i)
    print(f"Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}")


numbers = list(map(int, (input())))
even_odd_sum(numbers)
