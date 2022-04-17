substring = input().split(", ")
text = input()
result = [x for x in substring if x in text]
print(result)
