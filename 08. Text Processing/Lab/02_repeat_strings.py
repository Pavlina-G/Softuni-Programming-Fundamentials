text = input().split()
output = ''

for word in text:
    output += word * len(word)
print(output, end='')