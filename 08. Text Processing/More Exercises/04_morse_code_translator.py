def morse_code():
    info = input().split(' | ')
    my_list = []

    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                       'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                       '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    code_reversed = {value:key for key,value in morse_code_dict.items()}

    for word in info:
        new_text = ''.join(code_reversed.get(i) for i in word.split())
        my_list.append(new_text.upper())

    print(' '.join(my_list))


morse_code()
