# Python-Encryption

A lightweight XOR encryption and decryption tool built in Python.

## Overview

Python-Encryption is a university project that implements XOR encryption and decryption using Python. The project consists of two main scripts (`encryption.py` and `decryption.py`) that process text files using a user-provided key.

XOR encryption is a simple yet effective method for basic data protection. This implementation focuses on demonstrating the core concepts of symmetric encryption while maintaining a clean, educational codebase.

## How XOR Encryption Works

XOR (eXclusive OR) is a logical operation that takes two binary inputs and returns a true value (1) if exactly one of the inputs is true. The truth table for XOR:

| a   | b   | a ^ b |
| --- | --- | ----- |
| 0   | 0   | 0     |
| 0   | 1   | 1     |
| 1   | 0   | 1     |
| 1   | 1   | 0     |

The key property of XOR that makes it useful for encryption is its reversibility:

- If `A ^ B = C`, then `C ^ B = A`
- This means the same operation can be used for both encryption and decryption.

In this implementation, each character in the text is converted to its ASCII binary representation and then XOR-ed with the corresponding character from the key. The key is repeated as necessary to match the length of the input text.

## Features

- Simple command-line interface
- Encryption of plain text files
- Decryption of previously encrypted files
- Character-by-character XOR operation
- Key repetition for handling texts longer than the key

## Installation

No additional packages are required beyond a standard Python 3.x installation.

```bash
# Clone the repository
git clone https://github.com/cosmin-panescu/Python-XOR-Encryption

# Navigate to the project directory
cd Python-Encryption
```

## Usage

### Encryption

```bash
python encryption.py
```

The script will:

1. Read content from `not_crypted_text`
2. Prompt you to enter an encryption key
3. Perform XOR encryption
4. Save the encrypted content to `encrypted_text`

### Decryption

```bash
python decryption.py
```

The script will:

1. Read content from `encrypted_text`
2. Prompt you to enter the same key used for encryption
3. Perform XOR decryption
4. Save the decrypted content to `decrypted_text`

## Code Explanation

### encrypt.py

The encryption script performs the following steps:

1. Reads the input file
2. Gets a key from the user
3. Repeats the key to match the length of the input text
4. For each character in the text:
   - Converts both the character and corresponding key character to binary
   - Ensures both are 8-bit binary numbers (padding with leading zeros if necessary)
   - Performs XOR operation bit by bit
   - Writes the result to the output file

### decrypt.py

The decryption script:

1. Reads the encrypted file (containing binary 0s and 1s)
2. Gets the key from the user
3. Converts the key to binary
4. Performs XOR operation between the encrypted binary and the key's binary
5. Groups the result into 8-bit chunks and converts them back to ASCII characters
6. Writes the decrypted text to the output file

## Example

Original text in `not_crypted_text`:

```
Hello, my name is Cosmin!
```

With the key `secret`, after running `encryption.py`, the content is encrypted and stored as binary in `encrypted_text`.

After running `decryption.py` with the same key (`secret`), the original text is recovered in `decrypted_text`:

```
Hello, my name is Cosmin!
```

## Limitations

- The current implementation works with ASCII text only
- Key management is manual - the user needs to remember and securely store the key
- No file integrity verification is implemented
- The binary output format uses one character per bit, making encrypted files 8 times larger than the original

## Future Improvements

- Add command-line arguments for input/output files
- Add file integrity checks (hash verification)
- Optimize the storage format of encrypted data
- Add support for Unicode characters
- Implement stronger encryption algorithms as optional alternatives

## Acknowledgments

- This project was created as part of a university assignment
