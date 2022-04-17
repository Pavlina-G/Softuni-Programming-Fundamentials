def aliquot_sum(number):
    sum_num = 0
    perfect = False
    if number > 0:
        for num in range(1, number):
            if number % num == 0:
                sum_num += num
        if sum_num == number:
            perfect = True

    if perfect:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


numbers_inp = int(input())
print(aliquot_sum(numbers_inp))
