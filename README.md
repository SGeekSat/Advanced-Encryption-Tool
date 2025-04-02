# Advanced-Encryption-Tool
*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: Surat Satsangi

*INTERN ID*: CT08SUW

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

# ABOUT
Advanced Encryption Tool is a secure, user-friendly application for encrypting and decrypting sensitive files using AES-256 (Advanced Encryption Standard)encryption. This has been built with Streamlit, with which a simple web interface is provided that allows the users to protect their confidential documents, images, and other files with strong cryptographic security without requiring extensive technical knowledge.

# FEATURES

- AES-256 Encryption: Military-grade encryption standard for maximum security.

- User-Friendly Interface: Ckean, intuitive web interface powered by Streamlit

- File Versatility: Support for multiple file types including TXT, PDF, PNG, JPEG and Binary files.

- Password Protection: Custom secret jey input for personalized security.

- Integrity Verification: Authentication tag ensnures encrypted data hasn't been tempered with.

- Instant Download: Direct download for encrypted or decrypted files.

- Error Handling: Clear feedback when decryption fails due to incorrected keys or corrupted files.

# TECHNICAL IMPLEMENTATION

- Encryption Algorithm: Advanced Encryption Standard (AES) with 256-bit keys.

- Mode of Operation: EAX(Encrypt-then-Authenticate-then-Translate) prviding both confidentiality and authenticity.

- Nonce Management: Automatic generation and handling of cryptographic nonce.

- Authentication: Includes tag verification to ensure data integrity.

- Key Handling: Automatic padding/trunction to ensure proper key length.

# ENVIRONMENT AND REQUIREMENTS
- Python 3.6+

- Streamlit framework

- PyCryptodome library for AES implementation

- Web browser for accessing the interface

- No special hardware requirements

Can be downloaded from requriements.txt

# USAGE

1. Launch the application using Streamlit: streamlit run app.py

2. Select operation mode (Encrypt or Decrypt)

3. Upload the target file using file uploader

4. Enter a 32-character secret key( which can also be automatically adjusted)

5. Download the resulting encrypting or decrypting file

6. Store the secret key securely- if lost, encrypted data can't be recovered.

# SECURITY NOTE

This tool implements strong encryption that provides excellent protection for sensitive data. However:
- The security of the encrypted files depends on keeping the secret confidential.

- Always use strong and unique keys that are difficult to guess. Suggested is to use password manager to generate and store strong encryption keys.

- This tool is intended for legitmate personal and business use only.

