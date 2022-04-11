number = int(input())
start_num = ord("a") #97

for i in range(0,number):
    for j in range(0,number):
        for k in range(0,number):
            print(f"{chr(start_num + i)}{chr(start_num + j)}{chr(start_num + k)}")