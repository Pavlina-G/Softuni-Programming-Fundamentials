number = int(input())
is_prime_number = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime_number = False
            break
else:
    is_prime_number = False

print(f"{is_prime_number}")