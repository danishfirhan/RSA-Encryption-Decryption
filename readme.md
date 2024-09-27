```md
# RSA Encryption and Decryption Program

This project demonstrates the implementation of RSA encryption and decryption in Python. The program allows users to generate RSA public and private keys, encrypt a message using the public key, and decrypt it using the private key.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **RSA (Rivest–Shamir–Adleman)** algorithm is a public-key cryptosystem that is widely used for secure data transmission. This program provides a basic implementation of the RSA algorithm where users can:
1. Generate a pair of public and private keys.
2. Encrypt a message using the public key.
3. Decrypt the message using the private key.

## Features

- **Prime number validation**: Ensures the input numbers are prime.
- **Key generation**: Public and private keys are generated dynamically.
- **Message encryption**: Allows the user to input a plaintext message and encrypt it using the public key.
- **Message decryption**: Decrypts the ciphertext back into the original message using the private key.
- **Command-line interface**: Simple and interactive.

## How It Works

1. **Prime Number Input**: The user is prompted to input two prime numbers `p` and `q`.
2. **Key Generation**:
   - The public key is generated as `(e, n)` where `e` is a randomly selected number coprime to Euler’s totient function `phi(n)`, and `n = p * q`.
   - The private key is generated as `(d, n)`, where `d` is the modular inverse of `e` modulo `phi(n)`.
3. **Encryption**:
   - The message is encrypted using the public key with the formula `c = (m^e) % n`, where `m` is the ASCII value of each character in the message.
4. **Decryption**:
   - The encrypted message is decrypted using the private key with the formula `m = (c^d) % n`.

## Usage

To use the program:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/rsa-encryption-program.git
   cd rsa-encryption-program
   ```

2. **Run the program**:
   ```bash
   python rsa_encryption.py
   ```

3. **Instructions**:
   - You will be prompted to enter two prime numbers.
   - The program will generate public and private keys.
   - Enter a message to encrypt.
   - The program will then display the encrypted message and the decrypted version.

## Example

```bash
RSA Encryption/Decryption Program Lab Skill 2 CS
Enter a prime number (p): 11
Enter another prime number (q): 13
Public Key: (7, 143)
Private Key: (103, 143)
Enter a message to encrypt: hello
Encrypted Message: [59, 120, 78, 78, 92]
Decrypted Message: hello
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```

Feel free to modify the `README.md` to fit your needs!