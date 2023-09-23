from utils import *


def playfairCipher(text, key, sign):
    new_text = ""

    for i in range(len(text)):
        pos_1 = letterPosition(text[i][0], key)
        pos_2 = letterPosition(text[i][1], key)

        if pos_1[0] == pos_2[0]:

            # If the letters are on the same column
            # we shift them to the left one position
            # (mod 5 since we want to wrap around)
            new_text += key[pos_1[0]][(pos_1[1] + sign) % 5]
            new_text += key[pos_2[0]][(pos_2[1] + sign) % 5]

        elif pos_1[1] == pos_2[1]:

            # If the letters are on the same row
            # we shift them down one position
            new_text += key[(pos_1[0] + sign) % 5][pos_1[1]]
            new_text += key[(pos_2[0] + sign) % 5][pos_2[1]]

        else:

            # If the letters are on different rows and columns
            # we swap their positions
            new_text += key[pos_1[0]][pos_2[1]]
            new_text += key[pos_2[0]][pos_1[1]]

    return new_text


def letterPosition(char, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return [i, j]


def playfairEncryption(text, key):
    text = letterSeparation(text)
    text = letterAddition(text)
    key = keyToMatrix(key)
    return playfairCipher(text, key, 1)


def playfairDecryption(text, key):
    text = letterSeparation(text)
    key = keyToMatrix(key)
    return playfairCipher(text, key, -1)
