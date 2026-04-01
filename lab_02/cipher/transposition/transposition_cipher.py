def encrypt(text, key):
    cipher = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(text):
            cipher[col] += text[pointer]
            pointer += key

    return ''.join(cipher)


def decrypt(cipher, key):
    num_cols = int(len(cipher) / key)
    num_rows = key
    num_shaded = len(cipher) % key

    plaintext = [''] * num_cols

    col = 0
    row = 0

    for symbol in cipher:
        plaintext[col] += symbol
        col += 1

        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded):
            col = 0
            row += 1

    return ''.join(plaintext)