from public_key_algorithms import elgamal_encryption
import random

random.seed(0)

prime_number = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
generator = 2

private_key = random.randint(1, prime_number - 2)
public_key = pow(generator, private_key, prime_number)

hashed_message = "fad5c8fb7acf26e9eb25f894c18024909171befb73fe8a88e596fc88ff5a1a837dcf29e63cfca5c8"
original_message = """from these two fundamental principles for selecting usable field ciphers, kerckhoffs deduced six specific requirements: (1) the system should be, if not theoretically unbreakable, unbreakable in practice; (2) compromise of the system should not inconvenience the correspondents; (3) the key should be rememberable without notes and should be easily changeable; (4) the cryptograms should be transmissible by telegraph; (5) the apparatus or documents should be portable and operable by a single person; (6) the system should be easy, neither requiring knowledge of a long list of rules nor involving mental strain. These requirements still comprise the ideal which military ciphers aim at. They have been rephrased, and qualities that lie implicit have been made explicit. But any modern cryptographer would be very happy if any cipher fulfilled all six.  Of course, it has never been possible to do that. There appears to be a certain incompatibility among them that makes it impossible to institute all of them at once. The requirement that is usually sacrificed is the first. Kerckhoffs argued strongly against the notion of a field cipher that would simply resist solution long enough for the orders it transmitted to be carried out. This was not enough, he said, declaring that "the secret matter in communications sent over a distance very often retains its importance beyond the day on which it was transmitted." He was on the side of the angels, but a practical field cipher that is unbreakable was not possible in his day, nor is it today, and so military cryptography has settled for field ciphers that delay but do not defeat cryptanalysis. Perhaps the most startling requirement, at first glance, was the second. Kerckhoffs explained that by "system" he meant "the material part of the system; tableaux, code books, or whatever mechanical apparatus may be necessary," and not "the key proper." Kerckhoffs here makes for the first time the distinction, now basic to cryptology, between the general system and the specific key. Why must the general system "not require secrecy," as, for example, a codebook requires it? Why must it be "a process that... our neighbors can even copy and adopt"? Because, Kerckhoffs said, "it is not necessary to conjure up imaginary phantoms and to suspect the incorruptibility of employees or subalterns to understand that, if a system requiring secrecy were in the hands of too large a number of individuals, it could be compromised at each engagement in which one or another of them took part." This has proved to be true, and Kerckhoffs' second requirement has become widely accepted under a form that is sometimes called the fundamental assumption of military cryptography: that the enemy knows the general system. But he must still be unable to solve messages in it without knowing the specific key. In its modern formulation, the Kerckhoffs doctrine states that secrecy must reside solely in the keys. Had Kerckhoffs merely published his perceptions of the problems facing post-telegraph cryptography and his prescriptions for resolving them, he would have assured a place for himself in the pantheon of cryptology. But he did more. He contributed a technique of cryptanalysis that is of supreme importance today. Called "superimposition," it constitutes the most general solution for polyalphabetic substitution systems. With few exceptions, it lays no restrictions on the type or length of keys, as does the Kasiski method, nor on the alphabets, which may be interrelated or entirely independent. It wants only several messages in the same key. The cryptanalyst must align these one above the other so that letters enciphered with the same key letter will fall into a single column. In the simplest case, that of a running key (a very long continuous text used as a key, as a novel) that restarts with each message, he can do this simply by placing all the first letters in the first column, all the second letters in the next column, and so on.
"""


def sign_message(message_digest):
    k = 65537
    r = pow(generator, k, prime_number)
    s = pow(message_digest - private_key * r, 1, prime_number - 1)
    s = (s * pow(k, -1, prime_number - 1)) % (prime_number - 1)
    return r, s


def check_signature(message_digest, signed_message, r):
    if (r < 1) or (r > prime_number - 1):
        print("r is not in the range [1, prime_number - 1]")
        return False

    if (signed_message < 1) or (signed_message > prime_number - 1):
        print("Signed message is not in the range [1, prime_number - 1]")
        return False

    g = pow(generator, message_digest, prime_number)
    y = pow(public_key, r, prime_number)
    r = pow(r, signed_message, prime_number)
    obtained_message = (y * r) % prime_number
    if g == obtained_message:
        return True
    else:
        return False


def hash_to_decimal(message):
    message_hex = message.encode().hex()
    return int(message_hex, 16)


def main():
    print("Public key:"
          "\n1. ", prime_number,
          "\n2. ", generator,
          "\n3. ", public_key)
    message_digest = hash_to_decimal(hashed_message)
    r, signed_message = sign_message(message_digest)
    obtained_message = check_signature(message_digest, signed_message, r)

    print("\nHashed message:", hash_to_decimal(hashed_message))
    print("Signed message:", signed_message)
    if obtained_message:
        print("\nMessage is authentic")
    else:
        print("\nMessage is not authentic")


if __name__ == '__main__':
    main()
