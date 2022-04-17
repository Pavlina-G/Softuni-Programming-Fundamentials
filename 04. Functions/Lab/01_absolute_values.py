def abs_list():
    numbers = list(map(float, input().split(" ")))
    new_list = []

    for i in numbers:
        new_list.append(abs(i))
    print(new_list)

# abs_list()
#
# numbers = list(map(float, input().split(" ")))
# new_list = []
#
# for i in numbers:
#     new_list.append(abs(i))
#
# print(new_list)