
def encrypt(msg, e_key, semi_prime):
    list_encrypted = []

    for i in range(len(msg)):
        list_encrypted.append(pow(msg[i], e_key, semi_prime))

    return list_encrypted


def decrypt(cipher_text, d_key, semi_prime):
    list_decrypted = []

    for i in range(len(cipher_text)):
        list_decrypted.append(pow(cipher_text[i], d_key, semi_prime))

    return list_decrypted
