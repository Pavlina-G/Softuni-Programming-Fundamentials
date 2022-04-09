# year = int(input()) + 1
#
# while True:
#     year_str = str(year)
#     if len(year_str) == len(set(year_str)): # set has unique elements, len(set) =  shows only unique elements
#         print(year)
#         break
#     year += 1

year = int(input()) + 1

while len(set(str(year))) != len(str(year)):
    year += 1

print(year)


