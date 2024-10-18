from Crypto.Cipher import ARC4
import binascii
import itertools
import string

# Use case: to decrypt a ARC4 cipher given key length

# The ciphertext in hexadecimal format
ciphertext_hex = "6fce38f8836e82d446c3af46eb3a945a97bb8088256751e47f73a02943883165"

# Convert the hex string to bytes
ciphertext = binascii.unhexlify(ciphertext_hex)

# Function to decrypt with rc4
def decrypt_rc4(ciphertext, key):
    cipher = ARC4.new(key)  
    return cipher.decrypt(ciphertext)

# List that contains both uppercase and lowercase letters
charset = string.ascii_letters  

# Try all combinations of 4-character (change if needed) passwords with upper and lowercase letters 
for combo in itertools.product(charset, repeat=4):
    password = ''.join(combo).encode('utf-8') 
    decrypted = decrypt_rc4(ciphertext, password)
    
    try:
        # Decode to readable ASCII
        decoded = decrypted.decode('utf-8')
        print(f"Password: {password.decode()}, Decrypted message: {decoded}")
    except UnicodeDecodeError:
        continue
