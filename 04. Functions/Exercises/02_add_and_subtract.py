def sum_numbers(a, b):
    return a + b


def subtract(current_sum, c):
    return current_sum - c


num1, num2, num3 = int(input()), int(input()), int(input())
print(subtract(sum_numbers(num1, num2), num3))

