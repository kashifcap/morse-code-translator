morsecode = {
    'A' : '. -', 'B' : '- . . .', 'C' : '- . - .', 'D' : '- . .',
    'E' : '.', 'F' : '. . - .', 'G' : '- - .', 'H' : '. . . .',
    'I' : '. .', 'J' : '. - - -', 'K' : '- . -', 'L' : '. - . .',
    'M' : '- -', 'N' : '- .', 'O' : '- - -', 'P' : '. - - .',
    'Q' : '- - . -', 'R' : '. - .', 'S' : '. . .', 'T' : '-',
    'U' : '. . -', 'V' : '. . . -', 'W' : '. - -', 'X' : '- . . -',
    'Y' : '- . - -', 'Z' : '- - . .', '1' : '. - - - -', '2' : '. . - - -',
    '3' : '. . . - -', '4' : '. . . . -', '5' : '. . . . .', '6' : '- . . . .',
    '7' : '- - . . .', '8' : '- - - . .', '9' : '- - - - .', '0' : '- - - - -',
    ',' : '- - . . - -', '.' : '. - . - . -', '?' : '. . - - . .', '/' : '- . . - .',
    '-' : '- . . . . -', '(' : '- . - - .', ')' : '- . - - . -',
}

def encrypt(message):
    new_message = ''
    for letter in message:
        if letter != ' ':
            new_message += morsecode[letter] + ' '*3
        else:
            new_message += ' '*7
    return new_message

def decrypt(message):
    message += ' '
    new_message = ''
    alpha = ''
    i = 0
    for letter in message:
        if letter != ' ':
            if i ==1:
                alpha += ' '
            i = 0
            alpha += letter
        else:
            i += 1
            if i == 3:
                new_message += list(morsecode.keys())[list(morsecode.values()).index(alpha)]
                alpha =''
            if i == 7:
                new_message += ' '
    return new_message


if __name__ == "__main__":
    message = "Happy coding."
    n = encrypt(message.upper())
    print(n)
    print(decrypt(n))
