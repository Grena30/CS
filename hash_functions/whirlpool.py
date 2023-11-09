from public_key_algorithms import rsa_encryption

p = (83 * 2 ** 5318) - 1  # https://t5k.org/primes/page.php?id=38613
q = (5795 * 2 ** 5795) + 1  # https://t5k.org/primes/page.php?id=38112

n = p * q
phi = (p - 1) * (q - 1)
public_key = 65537
private_key = pow(public_key, -1, phi)

hashed_message = "758A1C39E5D78370400D5CA371268C90A290E88C0178B37C6282F15588EF81F0B318D4EDDAC98D45B828C195BA05B1120F0A4F0E8122A9B6EEDFC591848CD9E9"
original_message = """from these two fundamental principles for selecting usable field ciphers, kerckhoffs deduced six specific requirements: (1) the system should be, if not theoretically unbreakable, unbreakable in practice; (2) compromise of the system should not inconvenience the correspondents; (3) the key should be rememberable without notes and should be easily changeable; (4) the cryptograms should be transmissible by telegraph; (5) the apparatus or documents should be portable and operable by a single person; (6) the system should be easy, neither requiring knowledge of a long list of rules nor involving mental strain. These requirements still comprise the ideal which military ciphers aim at. They have been rephrased, and qualities that lie implicit have been made explicit. But any modern cryptographer would be very happy if any cipher fulfilled all six.  Of course, it has never been possible to do that. There appears to be a certain incompatibility among them that makes it impossible to institute all of them at once. The requirement that is usually sacrificed is the first. Kerckhoffs argued strongly against the notion of a field cipher that would simply resist solution long enough for the orders it transmitted to be carried out. This was not enough, he said, declaring that "the secret matter in communications sent over a distance very often retains its importance beyond the day on which it was transmitted." He was on the side of the angels, but a practical field cipher that is unbreakable was not possible in his day, nor is it today, and so military cryptography has settled for field ciphers that delay but do not defeat cryptanalysis. Perhaps the most startling requirement, at first glance, was the second. Kerckhoffs explained that by "system" he meant "the material part of the system; tableaux, code books, or whatever mechanical apparatus may be necessary," and not "the key proper." Kerckhoffs here makes for the first time the distinction, now basic to cryptology, between the general system and the specific key. Why must the general system "not require secrecy," as, for example, a codebook requires it? Why must it be "a process that... our neighbors can even copy and adopt"? Because, Kerckhoffs said, "it is not necessary to conjure up imaginary phantoms and to suspect the incorruptibility of employees or subalterns to understand that, if a system requiring secrecy were in the hands of too large a number of individuals, it could be compromised at each engagement in which one or another of them took part." This has proved to be true, and Kerckhoffs' second requirement has become widely accepted under a form that is sometimes called the fundamental assumption of military cryptography: that the enemy knows the general system. But he must still be unable to solve messages in it without knowing the specific key. In its modern formulation, the Kerckhoffs doctrine states that secrecy must reside solely in the keys. Had Kerckhoffs merely published his perceptions of the problems facing post-telegraph cryptography and his prescriptions for resolving them, he would have assured a place for himself in the pantheon of cryptology. But he did more. He contributed a technique of cryptanalysis that is of supreme importance today. Called "superimposition," it constitutes the most general solution for polyalphabetic substitution systems. With few exceptions, it lays no restrictions on the type or length of keys, as does the Kasiski method, nor on the alphabets, which may be interrelated or entirely independent. It wants only several messages in the same key. The cryptanalyst must align these one above the other so that letters enciphered with the same key letter will fall into a single column. In the simplest case, that of a running key (a very long continuous text used as a key, as a novel) that restarts with each message, he can do this simply by placing all the first letters in the first column, all the second letters in the next column, and so on.
"""


def sign_message(message_digest):
    return rsa_encryption.encrypt_rsa(hash_to_decimal(message_digest), private_key, n)


def check_signature(message_digest):
    return rsa_encryption.decrypt_rsa(message_digest, public_key, n)


def hash_to_decimal(message):
    message_hex = message.encode().hex()
    return int(message_hex, 16)


def main():
    print("Public key:", public_key)
    signed_message = sign_message(hashed_message)
    obtained_message = check_signature(signed_message)

    print("\nHashed message:", hash_to_decimal(hashed_message))
    print("\nSigned message:", signed_message)
    print("Obtained message:", obtained_message)

    if hash_to_decimal(hashed_message) == obtained_message:
        print("\nMessage is authentic")
    else:
        print("\nMessage is not authentic")


if __name__ == '__main__':
    main()
