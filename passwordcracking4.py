import hashlib

# Given hash
target_hash = "70d46181450828e775aa61239f792ed6"

# Base of the password
password_base = "SKY-BTST-"


def crack_password(target_hash):
    # Try all 4 digit combinations (0000 to 9999)
    for i in range(10000):
        # Format the number to 4 digits with leading zeros
        digits = f"{i:04}"
        # Form the complete password
        password = password_base + digits
        # Hash the password using MD5
        password_hash = hashlib.md5(password.encode()).hexdigest()
        # Check if the hash matches
        if password_hash == target_hash:
            return password
    return None


# Attempt to crack the password
cracked_password = crack_password(target_hash)
print(cracked_password)
