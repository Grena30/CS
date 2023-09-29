from primitive_functions import s_boxes, p_box


def convert_6bit_to_4bit(blocks):
    new_blocks = []

    for i in range(len(blocks)):

        block = blocks[i]
        s_box = s_boxes[i]

        exterior_bits = int(block[0] + block[5], 2)
        middle_bits = int(block[1:5], 2)
        new_block = s_box[exterior_bits][middle_bits]

        print(f"\nS-box {i + 1}:")

        for i in s_box:
            print(i)

        print("\nExterior bits (rows):", exterior_bits)
        print("Middle bits (columns):", middle_bits)
        print("New block number:", new_block, "->", format(new_block, "04b"))

        new_blocks.append(format(new_block, "04b"))

    return new_blocks


def permute_block(blocks):
    new_blocks = []
    blocks = "".join(blocks)

    print("\nP-box:")
    for i in p_box:
        print(i)

    for i in range(len(p_box)):
        row = p_box[i]
        new_block = ""

        for j in range(len(row)):
            new_block += blocks[row[j] - 1]

        new_blocks.append(new_block + " ")

    return new_blocks


def compute_nth_r(selection_blocks, left_blocks):
    r_blocks = []

    for i in range(len(selection_blocks)):
        selection_block = int(selection_blocks[i], 2)
        left_block = int(left_blocks[i], 2)

        xor_block = selection_block ^ left_block

        r_blocks.append(format(xor_block, "04b"))

    #r_blocks = map(str, r_blocks)

    return r_blocks
