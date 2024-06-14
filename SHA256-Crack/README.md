# SHA-256 Hash Cracker Tool

## Overview 🌟
This tool is specifically designed to perform brute-force attacks against SHA-256 hashed passwords. It aims to identify the plaintext password from a hashed version using a common wordlist.

## What is SHA-256? 🔍
SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function from the SHA-2 family. It generates a unique, fixed-size 256-bit (32-byte) hash. Used in various security applications and protocols, including TLS and SSL, SHA-256 is crucial for data integrity verification, digital signatures, and blockchain applications.

## What is Encryption and Decryption? 🔐
- **Encryption** is the process of converting plaintext into ciphertext, which is unreadable without the correct key, to protect the data's confidentiality.
- **Decryption** is the reverse process, converting the encrypted ciphertext back into readable plaintext, typically using a key.

## Purpose of the Script 🎯
This script is essential for security professionals to test the strength of passwords stored in SHA-256 format, often found in databases or used for securing user authentication mechanisms. By understanding how easily a password can be cracked, developers and security analysts can implement stronger security measures and password policies.

## How the Script Works 🛠️
1. **Command-Line Interface**: Users start the script by providing a SHA-256 hash as a command-line argument.
2. **Password File**: The script uses a pre-compiled list of potential passwords (`rockyou.txt`), a common choice for penetration testing due to its comprehensive collection of real-world passwords.
3. **Brute-Force Attack**: The script iterates through each password in the list, hashes it, and compares it against the provided hash. This process continues until a match is found or all passwords are tested.
4. **Progress Tracking**: Utilizes the `pwn` library's logging tools to provide real-time feedback on the number of attempts and current status.

## Features 🌈
- **Efficiency**: Streamlined to quickly hash and compare large numbers of passwords.
- **User Feedback**: Real-time updates on the brute-force process, enhancing user experience.
- **Success and Failure Notifications**: Clear, immediate feedback on whether the hash was cracked.

## Conclusion 🏁
Understanding the robustness of SHA-256 and the potential vulnerabilities in password management systems is vital for securing applications. This script serves as a practical tool for security testing, providing insights into the effectiveness of current cryptographic practices.

---
