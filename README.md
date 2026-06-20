# Caesar-Cipher-Tool
A Python implementation of the classic Caesar Cipher with full encrypt and decrypt functionality.

## What it does
- Encrypts plaintext by shifting each letter by a configurable 
  shift value (0–25)
- Decrypts ciphertext back to plaintext using reverse shift
- Handles uppercase and lowercase independently
- Preserves spaces, numbers, and special characters unchanged
- Uses modular arithmetic: `(ord(char) - base + shift) % 26`


## Security Context

Caesar cipher is not just a historical curiosity. Understanding it 
builds the foundation for:
- **ROT13** — used in CTFs constantly
- **Vigenère cipher** — polyalphabetic extension of Caesar
- **XOR encryption** — same modular logic, different operation
- **Modern block ciphers** — substitution is one of two core 
  operations in AES (substitution + permutation network)

   ## How to run
  1. Install Python 3
  2. Run python caesar cipher tool.py file code
  3. view encrypted and decrypted output
 
## Technical implementation

- Pure Python, no external libraries
- Modular arithmetic on ASCII values
- Handles both uppercase (`A=65`) and lowercase (`a=97`) ranges


  ## How to run
  1. Install Python 3
  2. Run python caesar cipher tool.py file code
  3. view encrypted and decrypted output
 
  ## What I learned

- Modular arithmetic applied to character encoding
- ASCII value manipulation in Python
- Why simple substitution ciphers are trivially broken 
  (frequency analysis — only 25 possible keys)
- Foundation for understanding modern symmetric encryption

 
 
