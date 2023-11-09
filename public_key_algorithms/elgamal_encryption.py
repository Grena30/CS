import random


def generate_public_key(prime_number, generator, private_key):
    return pow(generator, private_key, prime_number)


def encrypt_elgamal(msg, generator, public_key, prime_number):
    k = random.randint(2, prime_number - 2)
    r = pow(generator, k, prime_number)
    t = pow(public_key, k, prime_number)
    t = (t * msg) % prime_number

    return r, t


def decrypt_elgamal(t, r, private_key, prime_number):
    r = pow(r, -private_key, prime_number)

    return (r * t) % prime_number
