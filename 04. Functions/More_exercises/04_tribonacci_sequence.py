def tribonacci(num):
    # starting from 1 # the 4 num is sum of the 3 numbers before it
    if num == 1 or num == 2:
        return 1
    elif num == 3:
        return 2
    else:
        return tribonacci(num-1) + tribonacci(num-2) + tribonacci(num-3)


def trib(num):
    for i in range(1, num + 1):
        print(tribonacci(i), end=" ")


number = int(input())
trib(number)
