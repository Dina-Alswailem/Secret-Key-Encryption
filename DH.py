import sympy # sympy is a Python library for symbolic mathematics

# The Diffie-Hellman key exchange is a method for securely exchanging cryptographic keys over a public channel.
# first, calender the prime number and primitive root
def is_prime(n):
    if n < 2:
        return -1
    if n == 2:
        return 1
    for i in range(2, n):
        if n % i == 0:
            return -1
    return 1

def check_primitive_root(g, n):
    results = []
    for i in range(1, n):
        result = (g ** i) % n
        if result not in results:
            results.append(result)
    if len(results) == n - 1:
        return 1
    return -1

def find_primitive_root(n):
    for g in range(2, n):
        if check_primitive_root(g, n) == 1:
            return g
    return None

# Generate a random prime number
prime_number = sympy.randprime(20, 100)
print(f"Randomly generated prime number: {prime_number}")

# Find a primitive root for the prime number
primitive_root = find_primitive_root(prime_number)
if primitive_root is None:
    raise ValueError(f"No primitive root found for the prime number {prime_number}")

print(f"Calculated primitive root: {primitive_root}")

# Enter private keys
User1PrivKey = int(input("Enter the private key of User 1: "))
User2PrivKey = int(input("Enter the private key of User 2: "))

# Validate private keys
while User1PrivKey >= prime_number or User2PrivKey >= prime_number:
    print(f"The private keys must be less than {prime_number}.")
    User1PrivKey = int(input("Enter the private key of User 1: "))
    User2PrivKey = int(input("Enter the private key of User 2: "))

# Calculate public keys
User1PubKey = pow(primitive_root, User1PrivKey) % prime_number
User2PubKey = pow(primitive_root, User2PrivKey) % prime_number
print(f"\nUser 1's public key: {User1PubKey}\nUser 2's public key: {User2PubKey}\n")

# Calculate shared secret keys
User1SharedKey = pow(User2PubKey, User1PrivKey) % prime_number
User2SharedKey = pow(User1PubKey, User2PrivKey) % prime_number
print(f"\nUser 1's shared secret key: {User1SharedKey}\nUser 2's shared secret key: {User2SharedKey}\n")

# Verify the keys
if User1SharedKey == User2SharedKey:
    print("Keys have been exchanged successfully.")
else:
    print("Key exchange failed.")
