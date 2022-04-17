happiness_emp = list(map(int, input().split(" ")))
factor = int(input())

employees = list(map(lambda x: x * factor, happiness_emp))

# filter the elements that are greater than the average:
filtered = list(filter(lambda x: x >= sum(employees) / len(employees), employees))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(happiness_emp)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(happiness_emp)}. Employees are not happy!")