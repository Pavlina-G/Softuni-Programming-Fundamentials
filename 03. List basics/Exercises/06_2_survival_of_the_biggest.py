nums = input().split(" ")
copy_nums = list(map(int, nums)) # '1' -> int1,str 2 --> int 2

count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(", ".join(nums))