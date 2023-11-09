import random


def compute_private_key(prime_number):
    return random.randint(1, prime_number - 2)


def compute_public_value(prime_number, generator, a):
    return pow(generator, a, prime_number)


def compute_shared_secret(prime_number, A, b):
    return pow(A, b, prime_number)
