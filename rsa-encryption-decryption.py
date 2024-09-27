# RSA Encryption and Decryption Program

import random

# Calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Find modular inverse
def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

# Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generate RSA keys
def generate_keys():
    # Choose two random prime numbers
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    
    if p == q:
        raise ValueError("p and q must be different.")

    # Compute n = p * q
    n = p * q

    # Check if n is too small to handle ASCII characters
    if n < 128:
        raise ValueError("n is too small. Choose larger prime numbers.")

    # Compute Euler's Totient function: phi(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1 (public key exponent)
    e = random.randrange(2, phi)

    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate the private key d such that (d * e) % phi = 1
    d = mod_inverse(e, phi)

    # Public key (e, n) and private key (d, n)
    return (e, n), (d, n)

# Encrypt a message using the public key
def encrypt(message, public_key):
    e, n = public_key
    # Convert each character to its ASCII equivalent and encrypt using RSA formula: c = (m^e) % n
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Decrypt the message using the private key
def decrypt(encrypted_message, private_key):
    d, n = private_key
    # Decrypt each number using RSA formula: m = (c^d) % n
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Main function to demonstrate RSA
def main():
    print("RSA Encryption/Decryption Program Lab Skill 2 CS")

    # Generate public and private keys
    try:
        public_key, private_key = generate_keys()
        print(f"Public Key: {public_key}")
        print(f"Private Key: {private_key}")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    # Encrypt a message
    message = input("Enter a message to encrypt: ")
    encrypted_message = encrypt(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
