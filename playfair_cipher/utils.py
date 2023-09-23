import random

chars = ['Z', 'X', 'Q']
basicAlphabet = (list(map(chr, range(ord('A'), ord('Z') + 1))))


def textInput():
    while True:
        msg = input("Enter your message: ").replace(" ", "").upper()
        if len(msg) == 0:
            print("Your message should not be empty")
            continue

        if letterCheck(msg):
            return msg


def keyInput():
    while True:
        key = input("Enter key: ").replace(" ", "").upper()
        if len(key) < 7:
            print("Your key should contain 7 or more characters")
            continue

        if letterCheck(key):
            return key


def letterCheck(text):
    for i in range(len(text)):
        if text[i] not in basicAlphabet:
            print("Your text should contain only letters (a-z, A-Z)")
            return False

        if i == len(text) - 1:
            return True


def letterSeparation(msg):
    new_msg = []

    if len(msg) % 2 != 0:
        letter = random.choice(chars)
        msg = msg + letter

    msg = msg.upper()

    for i in range(0, len(msg), 2):

        if msg[i] == msg[i + 1] == "J":
            new_msg.append(["I", "I"])
        elif msg[i] == "J":
            new_msg.append([msg[i], "I"])
        elif msg[i + 1] == "J":
            new_msg.append(["I", msg[i + 1]])
        else:
            new_msg.append([msg[i], msg[i + 1]])

    return new_msg


def letterAddition(msg):
    digraphs = []

    for i in range(len(msg)):

        if msg[i][0] == msg[i][1]:
            letter = random.choice(chars)
            digraphs.append([msg[i][0], letter])

            letter = random.choice(chars)
            digraphs.append([msg[i][1], letter])
        else:
            digraphs.append([msg[i][0], msg[i][1]])

    return digraphs


def uniqueKey(key):
    new_key = ""

    for i in range(len(key)):
        if key[i] not in new_key:
            new_key += key[i]

    return new_key


def uniqueAlphabet(key):
    new_alphabet = key

    for i in basicAlphabet:
        if i == "J":
            continue

        if i not in new_alphabet:
            new_alphabet += i

    return new_alphabet


def keyToMatrix(key):
    key = uniqueKey(key)
    alphabet = uniqueAlphabet(key)
    matrix = []

    for i in range(5):
        matrix.append([])

        for j in range(5):
            matrix[i].append(alphabet[5 * i + j])

    return matrix

