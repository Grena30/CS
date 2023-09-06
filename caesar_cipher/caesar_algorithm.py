
# Create a list of characters from A to Z
basic_alphabet = (list(map(chr, range(ord('A'), ord('Z') + 1))))
# Transform the list into a string and removes spaces
basic_alphabet = ' '.join(basic_alphabet).replace(" ", "")


def valid_input():

    while 1:

        key = input("Enter key: ")

        try:
            return int(key)
        except:
            print("Input an integer key")


def key_alphabet(key=""):

    if not key:
        return basic_alphabet

    key = key.replace(" ", "").upper()

    # Combine the key with the basic_alphabet
    key += basic_alphabet
    new_alphabet = key[0]

    # Check for each unique element in key and if it's missing from new_alphabet add it
    for i in key:
        if i not in new_alphabet:
            new_alphabet += i

    return new_alphabet


def caesar_cipher(msg, key_1, sign_value, alphabet=key_alphabet()):

    new_msg = ""
    msg = msg.replace(" ", "").upper()

    for i in range(len(msg)):

        # Check for the index in the alphabet of the character msg[i]
        # Sign value of -1 represents decryption and 1 encryption
        pos = (alphabet.index(msg[i]) + sign_value * key_1) % 26
        new_msg += alphabet[pos]

    return new_msg

