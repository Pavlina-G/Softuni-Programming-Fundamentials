def character(a, b):
    output = []
    for i in range(ord(a) + 1, ord(b)):
        output.append(chr(i))
    print(" ".join(output))


char1 = input()
char2 = input()
character(char1, char2)