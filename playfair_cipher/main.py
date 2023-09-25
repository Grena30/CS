from utils import keyInput, textInput, keyToMatrix
from playfair_cipher import playfairEncryption, playfairDecryption


def main():
    while True:
        print("Playfair Cipher")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            msg = textInput()
            key = keyInput()
            print("\nMatrix: ")
            for i in keyToMatrix(key):
                print(i)
            print("\nEncrypted message:", playfairEncryption(msg, key), "\n")

        elif choice == 2:
            msg = textInput()
            key = keyInput()
            print("\nMatrix: ")
            for i in keyToMatrix(key):
                print(i)
            print("\nDecrypted message:", playfairDecryption(msg, key), "\n")

        elif choice == 3:
            break

        else:
            print("Unknown choice")


if __name__ == '__main__':
    main()
