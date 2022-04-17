even_string = list(map(int, input().split(", ")))
even_index_bool = map(lambda x: x if even_string[x] % 2 == 0 else 'no', range(len(even_string)))
even_index = list(filter(lambda a: a != 'no', even_index_bool))

print(even_index)