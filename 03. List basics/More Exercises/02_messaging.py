numbers = list(map(int, input().split(' ')))
text = input()

message = ""

for i in range(len(numbers)):
    sum_num = 0
    for j in str(numbers[i]):
        sum_num += int(j)
    index = sum_num

    if index > len(text):
        # index = index % len(text)
        index = index - len(text)
    message += text[index]

    new_text = text[:index] + text[index+1:]
    text = new_text

print(message)

