# 1 way:

# def factorials(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#
#     return result
#
#
# num1 = int(input())
# num2 = int(input())
# division = factorials(num1) /  factorials(num2)
# print(f"{division:.2f}")

# 2 way:
# def factorials(num):
#     return 1 if num == 0 or num == 1 else num * factorials(num - 1)
#
#
# num1 = int(input())
# num2 = int(input())
# division = factorials(num1) /  factorials(num2)
# print(f"{division:.2f}")

# 3 way
import math

def factorials(num):
    return math.factorial(num)


num1 = int(input())
num2 = int(input())
division = factorials(num1)/factorials(num2)
print(f"{division:.2f}")
