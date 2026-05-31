# Hash-Cracker-Python
Lightweight Python hash cracker with automatic hash type detection and multi-algorithm support.

# Python Hash Cracker

A simple and efficient Python script to crack cryptographic hashes using a wordlist (dictionary attack). The tool dynamically detects common hash types based on their length and supports fallback brute-force verification for unknown formats.

## Features
* **Auto-Detection:** Automatically recognizes MD5, SHA1, SHA256, and SHA512 based on hash string length.
* **Brute-Force Mode:** If the hash format is unknown, it tests the wordlist against all supported algorithms.
* **Nested Loop Processing:** Highly optimized iteration over multiple algorithms per candidate password.

## Prerequisites
Before running the script, ensure you have Python 3 installed. You will also need a wordlist file named `rockyou.txt` placed in the same directory as the script.

## Installation & Setup

1. Clone the repository or download the script file:
   ```bash
   git clone [https://github.com/x3bdulaziz/Hash-Cracker-Python.git](https://github.com/x3bdulaziz/Hash-Cracker-Python.git)
   cd Hash-Cracker-Python
