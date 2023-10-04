import random


def compute_private_key(prime_number):
    a = random.randint(1, prime_number - 2)

    return a


def compute_public_value(prime_number, generator, a):
    A = pow(generator, a, prime_number)

    return A


def compute_shared_secret(prime_number, A, b):
    shared_secret = pow(A, b, prime_number)

    return shared_secret


def compute_key_equality(shared_a, shared_b):
    if shared_a == shared_b:
        print("\nShared secret is equal")
    else:
        print("\nShared secret is not equal")
