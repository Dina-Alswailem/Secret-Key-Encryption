# the vignere cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. using the order of the number in the alphbet.

# first, we need to generate the encryption key by repeating the keyword until it matches the length of the plaintext
def generate_encryption_key(plaintext, keyword):
    keyword = list(keyword.upper())
    keyword_length = len(keyword)
    if len(plaintext) == keyword_length:
        return keyword
    else:
        extended_keyword = [keyword[i % keyword_length] for i in range(len(plaintext))]
        return ''.join(extended_keyword)

# to encrypt the text, we add the numerical values of the plaintext and keyword, then take the modulus of 26 to get the new numerical value of the encrypted text
def encrypt(plaintext, keyword):
    encrypted_text = []
    encryption_table = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i].upper()) + ord(keyword[i % len(keyword)].upper())) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
        encryption_table.append((plaintext[i], keyword[i % len(keyword)], chr(x)))
    print("Encryption Table:")
    for item in encryption_table:
        print(item[0], "+", item[1], "=", item[2])
    return ''.join(encrypted_text)

# to decrypt the text, we subtract the numerical values of the encrypted text and keyword, then take the modulus of 26 to get the new numerical value of the decrypted text
def decrypt(encrypted_text, keyword):
    decrypted_text = []
    decryption_table = []
    for i in range(len(encrypted_text)):
        x = (ord(encrypted_text[i]) - ord(keyword[i % len(keyword)]) + 26) % 26
        x += ord('A')
        decrypted_text.append(chr(x))
        decryption_table.append((encrypted_text[i], keyword[i % len(keyword)], chr(x)))
    print("Decryption Table:")
    for item in decryption_table:
        print(item[0], "-", item[1], "=", item[2])
    return ''.join(decrypted_text)

# receive input from the user and call the functions accordingly
input_text = input("Enter text to process: ")
keyword = input("Enter the keyword: ")
mode = input("Encrypt or Decrypt? (Type 'Encrypt' or 'Decrypt'): ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode. Please enter 'Encrypt' or 'Decrypt'.")
else:
    if mode == "encrypt":
        key = generate_encryption_key(input_text, keyword)
        print("Encryption Key Used: ", ''.join(key).upper())
        encrypted_text = encrypt(input_text, key)
        print("Encrypted Text: ", encrypted_text)
    else:
        key = generate_encryption_key(input_text, keyword)
        print("Decryption Key Used: ", ''.join(key).upper())
        print("Decrypted Text: ", decrypt(input_text, key))
