def find_all_dots(matrix):
    result = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '.':
                result.append((r, c))
    return result


rows = int(input())
matrix = [[x for x in input().split(' ')] for _ in range(rows)]
dots = find_all_dots(matrix)
deltas = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]
paths_dict = {}
max_len = 0

for dot in dots:
    paths_dict[dot] = set()
    dot_row, dot_col = dot
    for row, col in deltas:
        new_row = dot_row + row
        new_col = dot_col + col
        if (new_row, new_col) in dots:
            paths_dict[dot].add((new_row, new_col))
            for key, value in paths_dict.items():
                if dot in value:
                    paths_dict[key].add((new_row, new_col))
        else:
            continue

copy_dict = paths_dict.copy()

for key, value in paths_dict.items():
    for key2, values2 in copy_dict.items():
        if key in values2:
            copy_dict[key2].update(value)

for value in copy_dict.values():
    if len(value) > max_len:
        max_len = len(value)
print(max_len)
