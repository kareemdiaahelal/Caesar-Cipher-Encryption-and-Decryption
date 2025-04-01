```markdown
# Caesar Cipher Program

This is a Python implementation of the Caesar Cipher, a simple encryption and decryption algorithm. The program allows the user to encrypt and decrypt text using a shift key between 1 and 26. The Caesar Cipher works by shifting each letter of the alphabet by a specified number of positions.

## Features

- Encrypt and decrypt text using the Caesar Cipher.
- Input validation for shift key (must be between 1 and 26).
- Handle both uppercase and lowercase letters.
- Preserve non-alphabetic characters (e.g., spaces, punctuation).
- Easy-to-use command-line interface for encryption and decryption.

## How to Use

### 1. Clone the repository

To get started, first clone this repository to your local machine:

```bash
git clone https://github.com/kareeemdiaahelal/caesar-cipher.git
cd caesar-cipher
```

### 2. Run the Program

Run the Python program using the command:

```bash
python Code.py
```

### 3. Provide Input

The program will ask for the following inputs:

- **Text**: The text you want to encrypt or decrypt.
- **Shift Key**: A shift key between 1 and 26 to specify how much the alphabet letters should be shifted.
- **Operation**: Whether you want to encrypt or decrypt the text.

### Example

**Encrypting Text:**

```bash
Enter the text you want to encrypt or decrypt: Hello World
Enter the shift key (From 1 to 26): 3
Do you want to encrypt a plaintext or decrypt a ciphertext?
1: Encrypt
2: Decrypt
Choice: 1
Result: Khoor Zruog
```

**Decrypting Text:**

```bash
Enter the text you want to encrypt or decrypt: Khoor Zruog
Enter the shift key (From 1 to 26): 3
Do you want to encrypt a plaintext or decrypt a ciphertext?
1: Encrypt
2: Decrypt
Choice: 2
Result: Hello World
```

## Requirements

- Python 3.x or higher

## License

This project is open-source and available under the MIT License.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your code adheres to the existing style and includes tests for any new features.

---

### Author

[Kareem Diaa Helal](https://github.com/kareeemdiaahelal)
```