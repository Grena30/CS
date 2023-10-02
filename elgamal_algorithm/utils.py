from elgamal_encryption import *

import random

prime_number = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
generator = 2
private_key = random.randint(2, prime_number - 2)


def convert_to_hex(text_message):
    list_of_hex = []

    for i in range(len(text_message)):
        if ord(text_message[i]) > 255:
            raise ValueError("The message must be in ASCII format")

        list_of_hex.append(hex(ord(text_message[i]))[2:])

    return list_of_hex


def convert_hex_to_decimal(text_message_hex):
    list_of_decimal = []

    for i in range(len(text_message_hex)):
        list_of_decimal.append(int(text_message_hex[i], 16))

    return list_of_decimal


def enter_menu():
    while True:
        print("\nElGamal")
        print("1. Enter message")
        print("2. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print("\nEnter message:")

            msg = input()
            msg_hex = convert_to_hex(msg)
            msg_decimal = convert_hex_to_decimal(msg_hex)

            print("\nPrivate key:", private_key)

            beta_a = compute_beta_generator(prime_number, generator, private_key)
            print("\nBeta generator:", beta_a)

            r, t = encrypt(msg_decimal, generator, beta_a, prime_number)

            print("\nR:", r)
            print("\nEncrypted message:")
            for i in t:
                print(i)

            decrypted_msg = decrypt(t, r, private_key, prime_number)
            print("\nDecrypted message:", decrypted_msg)

            print("\nDecrypted message in ASCII format:")
            print("".join([chr(i) for i in decrypted_msg]))

        elif choice == 2:
            exit()
        else:
            print("\nInvalid choice")
