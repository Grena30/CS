import random
from des_cipher import *


def input_blocks(limit, power_of_two):
    blocks = []
    num_block = 1

    while True:
        block = input(f"Enter block {num_block}: ")

        try:
            block = int(block)
        except:
            print(f"Enter a valid number between 0 and {power_of_two - 1} (6-bit)")
            continue

        if block < 0 or block > pow(2, power_of_two) - 1:
            print(f"Enter a valid number between 0 and {pow(2, power_of_two) - 1} (6-bit)")
            continue

        num_block += 1

        block = format(block, f"0{power_of_two}b")
        blocks.append(block)

        if num_block > limit:
            break

    return blocks


def input_random_blocks(limit, power_of_two):
    blocks = []
    num_block = 1

    while True:
        block = random.randint(0, pow(2, power_of_two) - 1)

        num_block += 1

        block = format(block, f"0{power_of_two}b")
        blocks.append(block)

        if num_block > limit:
            break

    return blocks


def convert_input_blocks():
    print("\nSelection blocks")
    blocks = input_blocks(8, 6)
    print("\nInput selection blocks:", " ".join(blocks))

    print("\nLeft blocks")
    l_blocks = input_blocks(8, 4)

    blocks = convert_6bit_to_4bit(blocks)
    print("\nBlocks after selection functions:", " ".join(blocks))

    print("\nInput left blocks:", " ".join(l_blocks))

    return blocks, l_blocks


def convert_random_blocks():
    blocks = input_random_blocks(8, 6)
    print("\nRandom blocks:", " ".join(blocks))

    l_blocks = input_random_blocks(8, 4)

    blocks = convert_6bit_to_4bit(blocks)
    print("\nBlocks after selection functions:", " ".join(blocks))

    print("\nInput left blocks:", " ".join(l_blocks))

    return blocks, l_blocks


def enter_menu():
    while True:
        print("\nDES")
        print("1. Compute R")
        print("2. Exit")

        choice = int(input("\nEnter your choice: "))
        blocks = None

        if choice == 1:

            print("1. User input")
            print("2. Random input")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                blocks, l_blocks = convert_input_blocks()
            elif choice == 2:
                blocks, l_blocks = convert_random_blocks()
            else:
                print("Unknown choice")

            if blocks:
                permute_blocks = permute_block(blocks)
                print("\nBlocks after permutation:", "".join(permute_blocks))

                if l_blocks:
                    r_blocks = compute_nth_r(permute_blocks, l_blocks)
                    print("\nNth R block:", " ".join(r_blocks))

        elif choice == 2:
            break

        else:
            print("Unknown choice")
