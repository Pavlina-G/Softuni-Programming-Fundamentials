import re
import string

p= input()
valid = False

while not valid:
    if 6 < len(p) > 10:
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif re.search('[' + string.punctuation + ']+', p):
        break
    else:
        print("Valid Password")
        valid = True
        break

if not valid:
    print("Not a Valid Password")