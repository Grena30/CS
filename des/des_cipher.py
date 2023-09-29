from primitive_functions import s_boxes


def convert_6bit_to_4bit(blocks):
    new_blocks = []

    for i in range(len(blocks)):

        block = blocks[i]
        s_box = s_boxes[i]

        exterior_bits = int(block[0] + block[5], 2)
        middle_bits = int(block[1:5], 2)
        new_block = s_box[exterior_bits][middle_bits]

        print(f"\nS-box {i+1}:")

        for i in s_box:
            print(i)

        print("\nExterior bits (rows):", exterior_bits)
        print("Middle bits (columns):", middle_bits)
        print("New block number:", new_block, "->", format(new_block, "04b"))

        new_blocks.append(format(new_block, "04b"))

    return new_blocks
