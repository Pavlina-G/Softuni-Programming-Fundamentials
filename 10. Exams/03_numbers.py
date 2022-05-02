numbers = list(map(int, input().split(" ")))
average = sum(numbers) / len(numbers)

result = [x for x in numbers if x > average]
if len(result) == 0:
    print("No")
else:
    result.sort(reverse=True)
    print(*result[:5],sep=" ")

