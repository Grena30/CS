
def encrypt_rsa(msg, e_key, semi_prime):
    return pow(msg, e_key, semi_prime)


def decrypt_rsa(cipher_text, d_key, semi_prime):
    return pow(cipher_text, d_key, semi_prime)
