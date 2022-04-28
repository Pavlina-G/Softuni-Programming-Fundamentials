n = int(input())

for i in range(n):
    line = input()
    name = ''
    age = ''
    start_name = 0
    end_name = 0
    start_age = 0
    end_age = 0

    for ch in line:
        if ch == '@':
            start_name = line.index(ch)
        if ch == '|':
            end_name = line.index(ch)
        name = line[start_name + 1:end_name]

        if ch == '#':
            start_age = line.index(ch)
        if ch == '*':
            end_age = line.index(ch)
        age = line[start_age + 1:end_age]

    print(f"{name} is {age} years old.")
