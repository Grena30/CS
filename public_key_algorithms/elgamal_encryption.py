import random


def compute_beta_generator(prime_number, generator, private_key):
    beta_a = pow(generator, private_key, prime_number)

    return beta_a


def encrypt_elgamal(msg, generator, beta_generator, prime_number):
    k = random.randint(2, prime_number - 2)
    r = pow(generator, k, prime_number)

    new_msg = []
    for i in range(len(msg)):
        t = pow(beta_generator, k, prime_number)
        t = (t * msg[i]) % prime_number
        new_msg.append(t)

    return r, new_msg


def decrypt_elgamal(t, r, private_key, prime_number):

    r = pow(r, -private_key, prime_number)
    new_msg = []

    for i in range(len(t)):
        new_msg.append((r * t[i]) % prime_number)

    return new_msg
