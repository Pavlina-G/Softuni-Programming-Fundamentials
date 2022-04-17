def group_of_10(nums):
    group = []
    boundary = 10

    while len(nums) > 0:
        group = list(filter(lambda x: x <= boundary, nums))

        for num in group:
            nums.remove(num)

        print(f"Group of {boundary}'s: {group}")
        boundary += 10

numbers = list(map(int, input().split(", ")))
group_of_10(numbers)

