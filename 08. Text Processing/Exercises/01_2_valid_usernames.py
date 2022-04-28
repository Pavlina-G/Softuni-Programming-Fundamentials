import string
def valid_username(data):

    expected_elements = string.digits + string.ascii_letters + '-' + '_'
    # print(expected_elements) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_

    for name in data:
        valid = False
        if 3 <= len(name) <= 16:
            for char in name:
                if char not in expected_elements:
                    valid = False
                    break
                else:
                    valid = True
        if valid:
            print(name)


names = input().split(', ')
valid_username(names)