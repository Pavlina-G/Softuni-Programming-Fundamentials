import string
def valid_username(data):

    expected_elements = string.digits + string.ascii_letters + '-' + '_'

    for name in data:
        flag = 0
        if 3 > len(name) or len(name) > 16:
            flag = 1
        elif len([x for x in name if x in expected_elements]) != len(name):
            flag = 1
        elif flag == 0:
            print(name)


names = input().split(', ')
valid_username(names)
