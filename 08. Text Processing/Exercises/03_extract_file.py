text = input().split('\\')
data = text[-1].split('.')
print(f'File name: {data[0]}')
print(f'File extension: {data[1]}')
