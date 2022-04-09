divisor = int(input())
boundary = int(input())

the_largest_divisible_number = 0

if boundary // divisor == 0:
    print(boundary)
elif boundary // divisor < 0:
    pass
else:
    the_largest_divisible_number = boundary // divisor
    the_largest_divisible_number *= divisor
    print(the_largest_divisible_number)


