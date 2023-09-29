import random
from des_cipher import convert_6bit_to_4bit


def input_blocks():
    blocks = []
    num_block = 1

    while True:
        block = input(f"Enter block {num_block}: ")

        try:
            block = int(block)
        except:
            print("Enter a valid number between 0 and 63 (6-bit)")
            continue

        if block < 0 or block > 63:
            print("Enter a valid number between 0 and 63 (6-bit)")
            continue

        num_block += 1

        block = format(block, "06b")
        blocks.append(block)

        if num_block > 8:
            break

    return blocks


def input_random_blocks():
    blocks = []
    num_block = 1

    while True:
        block = random.randint(0, 63)

        num_block += 1

        block = format(block, "06b")
        blocks.append(block)

        if num_block > 8:
            break

    return blocks


def enter_menu():
    while True:
        print("\nDES")
        print("1. User input")
        print("2. Random input")
        print("3. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            blocks = input_blocks()
            print("\nBlocks:", " ".join(blocks))

            blocks = convert_6bit_to_4bit(blocks)
            print("\nBlocks after selection functions:", " ".join(blocks))

        elif choice == 2:
            blocks = input_random_blocks()
            print("\nRandom blocks:", " ".join(blocks))

            blocks = convert_6bit_to_4bit(blocks)
            print("\nBlocks after selection functions:", " ".join(blocks))

        elif choice == 3:
            break

        else:
            print("Unknown choice")
