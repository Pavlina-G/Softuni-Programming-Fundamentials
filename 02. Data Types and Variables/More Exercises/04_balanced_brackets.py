lines = int(input())

is_balanced = True
is_open = False

for i in range(1, lines + 1):
    input_str = input()

    if input_str == "(":
        if not is_open:
            is_open = True
        else:
            is_balanced = False

    if input_str == ")":
        if is_open:
            is_open = False
        else:
            is_balanced = False

if is_balanced and not is_open:
    print("BALANCED")
else:
    print("UNBALANCED")

