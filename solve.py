from Crypto.Cipher import ARC4
import binascii
import itertools
import string

# The ciphertext in hexadecimal format
ciphertext_hex = "6fce38f8836e82d446c3af46eb3a945a97bb8088256751e47f73a02943883165"

# Convert the hex string to bytes
ciphertext = binascii.unhexlify(ciphertext_hex)

# Function to try each 4-character password
def decrypt_rc4(ciphertext, key):
    cipher = ARC4.new(key)  
    return cipher.decrypt(ciphertext)

# Generate all possible combinations of 4-character passwords with upper and lowercase letters
charset = string.ascii_letters  # Contains both uppercase and lowercase letters

# Try all combinations
for combo in itertools.product(charset, repeat=4):
    password = ''.join(combo).encode('utf-8')  # Convert the password to bytes
    decrypted = decrypt_rc4(ciphertext, password)
    
    try:
        # Attempt to decode the result to see if it's readable
        decoded = decrypted.decode('utf-8')
        print(f"Password: {password.decode()}, Decrypted message: {decoded}")
    except UnicodeDecodeError:
        # If it can't be decoded to UTF-8, it probably isn't the correct password
        continue
