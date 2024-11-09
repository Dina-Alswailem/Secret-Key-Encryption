# the playfair cipher is a digraph substitution cipher
# that encrypts pairs of letters instead of single letters

#first, we need to generate a key square of letters that is 5*5
def generate_key_square(key):
    key = key.upper().replace("J", "I")
    key_square = ""
    for char in key:
        if char not in key_square and char != 'J':
            key_square += char
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_square:
            key_square += char
    return [key_square[i:i+5] for i in range(0, 25, 5)]

#next, we need to preprocess the plaintext by removing non-alphabetic characters, then grouping the letters into pairs, and adding a Z at the end if the last pair has only one letter or to seprate duplicate letters
def preprocessTXT(plaintext):
    plaintext = plaintext.upper()
    plaintext = "".join(filter(str.isalpha, plaintext))
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            plaintext_pairs.append(plaintext[i] + 'Z')
            i += 1
        else:
            plaintext_pairs.append(plaintext[i] + plaintext[i + 1])
            i += 2
    if len(plaintext_pairs[-1]) == 1:
        plaintext_pairs[-1] += 'Z'
    return plaintext_pairs

#next, we need to find the position of a letter in the key square
def find_position(key_square, letter):
    for i in range(5):
        for j in range(5):
            if key_square[i][j] == letter:
                return i, j

#next, to encrypt a bigram, we need to find the positions of the letters in the key square, then apply the following rules:
#1. if the letters are in the same row, replace them with the letters to their immediate right
#2. if the letters are in the same column, replace them with the letters immediately below
#3. if the letters are in different rows and columns, replace them with the letters on the same row but at the opposite corners of the rectangle defined by the original positions

def encrypt_bigram(key_square, bigram):
    a, b = bigram[0], bigram[1]
    row_a, col_a = find_position(key_square, a)
    row_b, col_b = find_position(key_square, b)
    if row_a == row_b:
        return key_square[row_a][(col_a + 1) % 5] + key_square[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return key_square[(row_a + 1) % 5][col_a] + key_square[(row_b + 1) % 5][col_b]
    else:
        return key_square[row_a][col_b] + key_square[row_b][col_a]

#next, to decrypt a bigram, we need to find the positions of the letters in the key square, then apply the same rules as above but in reverse
def decrypt_bigram(key_square, bigram):
    a, b = bigram[0], bigram[1]
    row_a, col_a = find_position(key_square, a)
    row_b, col_b = find_position(key_square, b)
    if row_a == row_b:
        return key_square[row_a][(col_a - 1) % 5] + key_square[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return key_square[(row_a - 1) % 5][col_a] + key_square[(row_b - 1) % 5][col_b]
    else:
        return key_square[row_a][col_b] + key_square[row_b][col_a]

# here, we define the functions to encrypt and decrypt the text using the functions defined above
def encrypt_text(plaintext, key):
    key_square = generate_key_square(key)
    plaintext_pairs = preprocessTXT(plaintext)
    ciphertext = ""
    for bigram in plaintext_pairs:
        ciphertext += encrypt_bigram(key_square, bigram)
    return key_square, plaintext_pairs, ciphertext

def decrypt_text(ciphertext, key):
    key_square = generate_key_square(key)
    ciphertext_pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plaintext = ""
    for bigram in ciphertext_pairs:
        plaintext += decrypt_bigram(key_square, bigram)
    return plaintext

# receive input from the user and call the functions accordingly
input_text = input("Enter text to process: ")
keyword = input("Enter keyword: ")
mode = input("Encrypt or decrypt? (Type 'encrypt' or 'decrypt'): ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
else:
    if mode == "encrypt":
        key_square, plaintext_pairs, encrypted_text = encrypt_text(input_text, keyword)
        print("Key Square:")
        for row in key_square:
            print(" ".join(row))
        print("\nOriginal Text Segmented:")
        for bigram in plaintext_pairs:
            print(bigram)
        print("\nEncrypted Text:", encrypted_text)
    else:
        decrypted_text = decrypt_text(input_text, keyword)
        print("Decrypted Text(minus the z at the end):", decrypted_text)
