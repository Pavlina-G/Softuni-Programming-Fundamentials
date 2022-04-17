first_line = list(map(int, input().split(' ')))
second_line = list(map(int, input().split(' ')))
third_line = list(map(int, input().split(' ')))

#create lists for each row

row1 = first_line
row2 = second_line
row3 = third_line

#create lists for each column
col1 = [row1[0], row2[0], row3[0]]
col2 = [row1[1], row2[1], row3[1]]
col3 = [row1[2], row2[2], row3[2]]

#create lists for diagonals

d1 = [row1[0], row2[1], row3[2]]
d2 = [row1[2], row2[1], row3[0]]

if row1.count(1) == 3 or row2.count(1) == 3 or row3.count(1) == 3 or \
        col1.count(1) == 3 or col2.count(1) == 3 or col3.count(1) == 3 \
        or d1.count(1) == 3 or d2.count(1) == 3:
    print("First player won")

elif row1.count(2) == 3 or row2.count(2) == 3 or row3.count(2) == 3 or \
        col1.count(2) == 3 or col2.count(2) == 3 or col3.count(2) == 3 \
        or d1.count(2) == 3 or d2.count(2) == 3:
    print('Second player won')
else:
    print("Draw!")



