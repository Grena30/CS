from diffie_hellman_key_exchange import *

prime_number = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
generator = 2


def generate_key_exchange():

    print("\nDiffie-Hellman Key Exchange")

    print("\nPrime number:", prime_number)
    print("Generator:", generator)

    a = compute_private_key(prime_number)
    b = compute_private_key(prime_number)
    print("\nPrivate keys:")
    print("a:", a)
    print("b:", b)

    A = compute_public_value(prime_number, generator, a)
    B = compute_public_value(prime_number, generator, b)
    print("\nPublic values:")
    print("A:", A)
    print("B:", B)

    shared_a = compute_shared_secret(prime_number, B, a)
    shared_b = compute_shared_secret(prime_number, A, b)
    print("\nShared secrets:")
    print("Shared A:", shared_a)
    print("Shared B:", shared_b)

    compute_key_equality(shared_a, shared_b)

