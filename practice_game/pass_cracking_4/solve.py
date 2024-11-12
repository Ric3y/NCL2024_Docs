import hashlib

# Base of the password
password_base = "SKY-BTST-"

def crack_password(target_hashes):
    results = {}
    
    # Try all 4-digit combinations (0000 to 9999)
    for i in range(10000):
        # Format the number to 4 digits with leading zeros
        digits = f"{i:04}"
        # Form the complete password
        password = password_base + digits
        # Hash the password using MD5
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        # Check each target hash
        for target_hash in target_hashes:
            if password_hash == target_hash:
                results[target_hash] = password

    return results

# Function to read hashes from a file and crack them
def crack_passwords_from_file(filename):
    with open(filename, 'r') as file:
        target_hashes = [line.strip() for line in file.readlines()]
    
    return crack_password(target_hashes)

results = crack_passwords_from_file('hashes.txt')
for hash_value, password in results.items():
    print(f"Hash: {hash_value} -> Cracked Password: {password}")

