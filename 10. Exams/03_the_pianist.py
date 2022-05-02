def add_func(piano_dict, piece, key, composer):
    if piece in piano_dict:
        print(f"{piece} is already in the collection!")
    else:
        piano_dict[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")

    return piano_dict


def remove_func(piano_dict, piece):

    if piece in piano_dict:
        piano_dict.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return piano_dict


def change_func(piano_dict, piece, new_key):
    if piece in piano_dict:
        composer = piano_dict[piece][0]
        piano_dict[piece] = [composer, new_key]
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return piano_dict

def stop_func(piano_dict):

    for piece, values in piano_dict.items():

        print(f"{piece} -> Composer: {values[0]}, Key: {values[1]}")


def pianist():
    n = int(input())
    piano_dict = {}

    for i in range(n):
        pieces = input().split("|")
        piano_dict[pieces[0]] = [pieces[1], pieces[2]]

    while True:
        command = input().split('|')
        if command[0] == 'Stop':
            stop_func(piano_dict)
            break

        piece = command[1]

        if command[0] == "Add":
            composer = command[2]
            key = command[3]
            piano_dict = add_func(piano_dict, piece, key, composer)

        elif command[0] == "Remove":
            piano_dict = remove_func(piano_dict, piece)

        elif command[0] == "ChangeKey":
            new_key = command[2]
            piano_dict = change_func(piano_dict, piece, new_key)


pianist()
