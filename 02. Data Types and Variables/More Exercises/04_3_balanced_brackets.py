lines = int(input())

last_bracket = ''
is_balanced = True

for i in range(1, lines + 1):
    input_str = input()

    if input_str == last_bracket or last_bracket == "" and input_str == ")":
        is_balanced = False

    last_bracket = input_str

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")