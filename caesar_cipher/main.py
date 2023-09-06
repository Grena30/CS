from caesar_algorithm import *


print("\nCaesar Cipher")

alphabet = basic_alphabet
key_1 = ""
key_2 = ""
msg = ""

while 1:

    print("\nMenu")
    print("1. Enter first key")
    print("2. Enter second key")
    print("3. Enter your encrypted/non-encrypted message")
    print("4. Print input data")
    print("5. Reset input data")
    print("6. Encrypt message")
    print("7. Decrypt  message")
    print("8. Exit")

    num = input("\nEnter your choice: ")

    match num:
        case "1":
            key_1 = valid_input()

        case "2":
            key_2 = input("Enter your key (Should be a word): ")
            alphabet = key_alphabet(key_2)

        case "3":
            msg = input("Enter your message: ")

        case "4":
            print("\nMessage:", msg)
            print("Key1:", key_1)
            print("Key2:", key_2)
            print("Alphabet:", alphabet)

        case "5":
            alphabet = basic_alphabet
            key_1 = ""
            key_2 = ""
            msg = ""

        case "6":
            sign = 1
            new_msg = caesar_cipher(msg, key_1, sign, alphabet)
            print("\nEncrypted message: ", new_msg)

        case "7":
            sign = -1
            new_msg = caesar_cipher(msg, key_1, sign, alphabet)
            print("\nDecrypted message: ", new_msg)

        case "8":
            exit(1)

        case _:
            print("Invalid input")
