import string
def validator(password):
    valid = True

    if not 10 >= len(password) >= 6:
        print("Password must be between 6 and 10 characters")
        valid = False
    if not any(char.isalpha() for char in password) or any(char in string.punctuation for char in password):
        print("Password must consist only of letters and digits")
        valid = False
    if not sum(map(lambda x: x.isdigit(), password)) >= 2:
        print('Password must have at least 2 digits')
        valid = False
    if valid:
        print("Password is valid")


password_inp = list(input())
validator(password_inp)
