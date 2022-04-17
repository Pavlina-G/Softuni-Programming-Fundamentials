rows_number = int(input())
rows = []
columns = []

for row in range(rows_number):
    list_row = list(map(int, input().split(" ")))
    rows.append(list_row)

columns = list(map(list, zip(*rows)))

battle = input().split(" ")
destroyed_ships = 0
coord_list = rows + columns

for k in battle:
    attack = k.split("-")
    a = int(attack[0])
    b = int(attack[1])

    if coord_list[a][b] > 0:
        coord_list[a][b] -= 1
        if coord_list[a][b] == 0:
            destroyed_ships += 1

print(destroyed_ships)

