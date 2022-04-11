# number_of_snowball = int(input())
# the_highest_value = 0
#
# the_best_weight = 0
# the_best_time = 0
# the_best_quality = 0
#
# for i in range(1, number_of_snowball + 1):
#
#     snowball_weight = int(input())
#     time_to_the_target = int(input())
#     quality = int(input())
#
#     snowball_value = int(snowball_weight / time_to_the_target) ** quality
#
#     if snowball_value > the_highest_value:
#         the_highest_value = snowball_value
#         the_best_time = time_to_the_target
#         the_best_quality = quality
#         the_best_weight = snowball_weight
#
# print(f"{the_best_weight} : {the_best_time} = {the_highest_value} ({the_best_quality})")

number_of_snowball = int(input())
the_highest_value = 0
the_best_snowball_data = 0

for i in range(1, number_of_snowball + 1):

    snowball_weight = int(input())
    time_to_the_target = int(input())
    quality = int(input())

    snowball_value = int(snowball_weight / time_to_the_target) ** quality

    if snowball_value > the_highest_value:
        the_highest_value = snowball_value
        the_best_snowball_data = f"{snowball_weight} : {time_to_the_target} = {the_highest_value} ({quality})"

print(the_best_snowball_data)