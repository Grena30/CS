import hashlib
import random

from rsa_encryption import *
from elgamal_encryption import *
from diffie_hellman_key_exchange import *

random.seed(724)

# RSA constants
# Selected primes from:
# https://t5k.org/primes/page.php?id=132936
# https://t5k.org/primes/page.php?id=119628

prime_number_1 = 504047074759976118362547213552326856111518250282791249968689378546454471112442645866195532219135552041345389747204292449265409915836497721507952344009757242788240584063503764684489985460308742669359621071799174032348712734258157028016604992715699241697547658556542474798611154943983653568291994326093161944916801118384228787027551888897849623202058134960267950604222207288148566763784952327266881451439184277973203721222998115019155681702853870152476388072244695575506646328487221506854617829891183769572282612426996308723685764097537799414305379062161557822129126028420564531807037889375066435098010694340412681411620468492229703855456565360976603082550926713897839604660053993122379355583349153225954412299314963762214846663651864140760446652658216296494460851357087839373298574324234466322396158453195718040542531882095274210728103232799993257351380901672006208870950318361308281877014179905757590437230195560903759928270997297858251426307637993597502893892889229276228661051698247606403744945344626150437088999039
prime_number_2 = 1264906703566737711594719870801915218395598824601474232734807958732336012552378499047462656026382640022163914348448136367416698669468565477104491064348229568733731262810267149896072183825857178043349952209317172654570333505698901209079886179756891559076225153981649979810167529818859202728902988457985201964208812285819316012488850272614234876136900093285930195277515873749068733858970727099479039085374902383882386839728528730457834024698697123060814984224223675669957213407330366012083493906367409384366890041672336198023041732674641629938135233485228301660793907283061419228798581265312661443408917185736851908731245638167040696655786591636101464459846718260817679360853385800897430264581694694308045680275968366084861446971625209710068957091591194320388081066900784861833691907620960410184912924658608050639718167900354460594514247885657611768805762807261844856956972819115528803514238603317477410348248893502757967196544235778135870007633166897342528153629947198081776158055962852980340265874848100433465447

n = prime_number_1 * prime_number_2
n_totient = (prime_number_1 - 1) * (prime_number_2 - 1)

# Public exponent needs to be coprime
public_exponent = 65537
private_key_rsa = pow(public_exponent, -1, n_totient)

# Shared constants Elgamal & Diffie-Hellman
prime_number = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
generator = 2

# ElGamal constants
private_key_elgamal = random.randint(2, prime_number - 2)


def key_to_256_bits(shared_secret):
    shared_key_bytes = shared_secret.to_bytes((shared_secret.bit_length() + 7) // 8, byteorder='big')
    return hashlib.sha256(shared_key_bytes).digest()


def compute_rsa():
    message = input("\nEnter message: ")
    message_hex = message.encode().hex()
    message_decimal = int(message_hex, 16)

    print("\nPrime number 1:", prime_number_1)
    print("Prime number 2:", prime_number_2)
    print("Result:", n)
    print("Totient:", n_totient)

    print("\nPrivate key:", private_key_rsa)
    print("Public exponent:", public_exponent)

    encrypted_message = encrypt_rsa(message_decimal, public_exponent, n)
    print("\nEncrypted message:", encrypted_message)

    decrypted_message = decrypt_rsa(encrypted_message, private_key_rsa, n)
    print("\nDecrypted message:", decrypted_message)

    print("\nDecrypted message in ASCII format:")
    string_result = bytes.fromhex(hex(decrypted_message)[2:]).decode("ASCII")
    print(string_result)


def compute_elgamal():
    message = input("\nEnter message: ")
    message_hex = message.encode().hex()
    message_decimal = int(message_hex, 16)

    print("\nPrivate key:", private_key_elgamal)

    public_key = generate_public_key(prime_number, generator, private_key_elgamal)
    print("Public key:", public_key)

    r, encrypted_message = encrypt_elgamal(message_decimal, generator, public_key, prime_number)

    print("R:", r)
    print("\nEncrypted message:", encrypted_message)

    decrypted_message = decrypt_elgamal(encrypted_message, r, private_key_elgamal, prime_number)
    print("\nDecrypted message:", decrypted_message)

    print("\nDecrypted message in ASCII format:")
    string_result = bytes.fromhex(hex(decrypted_message)[2:]).decode("ASCII")
    print(string_result)


def compute_diffie_hellman():
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

    if shared_a == shared_b:
        print("\nShared secrets are equal")
        new_key = int(key_to_256_bits(shared_a).hex(), 16)
        print("New key:", new_key)

    else:
        print("\nShared secrets are not equal")


def enter_menu():
    while True:
        print("\nPublic Key Algorithms")
        print("1. RSA Algorithm")
        print("2. ElGamal Algorithm")
        print("3. Diffie-Hellman Algorithm")
        print("4. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            compute_rsa()
        elif choice == 2:
            compute_elgamal()
        elif choice == 3:
            compute_diffie_hellman()
        elif choice == 4:
            exit()
        else:
            print("\nInvalid choice")
