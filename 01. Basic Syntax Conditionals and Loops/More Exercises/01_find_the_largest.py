
from itertools import combinations

# number = list(input())
# number.sort(reverse=True)
# print(''.join(number))

number = input()
list_number = sorted(str(number), reverse=True) # sorted function creates list of values/digits

for digit in list_number:
    print(digit, end="")
