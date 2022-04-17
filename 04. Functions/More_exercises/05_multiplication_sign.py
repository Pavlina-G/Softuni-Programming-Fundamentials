def multiplication_sign(a,b,c):
    new_list = [a, b, c]
    positive_count = [x for x in new_list if x > 0]
    negative_count = [x for x in new_list if x < 0]


    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    elif len(positive_count) == 3:
        return "positive"
    elif len(positive_count) == 1 and len(negative_count) == 2:
        return "positive"
    else:
        return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(multiplication_sign(num1, num2, num3))