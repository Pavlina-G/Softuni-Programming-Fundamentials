def smallest_num(num1, num2, num3):
    return min([num1, num2, num3])
    #return min((num1, num2, num3))


number1, number2, number3 = int(input()), int(input()),int(input())
print(smallest_num(number1, number2, number3))