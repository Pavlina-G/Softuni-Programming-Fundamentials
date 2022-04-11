nums = input().split(" ")
new_list = []

for num in nums:
    if int(num) > 0 :
        new_list.append(-int(num))
    else:
        new_list.append(abs(int(num)))

print(new_list)

nums = [-num if num > 0 else abs(num)for num in list(map(int(input().split(" "))))]
print(nums)
# map - обхожда това,което сме му дали отдясно, подобно на циклите и
# превръща например стринг в инт