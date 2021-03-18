# Ciphernotes

Encrypt or decrypt multiple txt files with a single AES encryption key.

## Requirements

Windows 10 and .NET 5 runtime, along with Python 3.
The `csencryption` program provided requires the `.NET 5` runtime.

## Encryption

1. Place plaintext files under the `plain` directory. 
2. Run the `encrypt_all.py` script and provide your secret key.

    ```
    python encrypt_all.py mySecretKey
    ```
    Files are now generated in the `cipher` folder. These files can be shared to anyone and they
    can only decrypt them if they know your secret key.
    Encrypted files have `_cipher` appended to their name.


## Decryption

1. Place cipher text files under the `cipher` directory.
2. Run the `decrypt_all.py` script and provide your secret key.
   ```
   python decrypt_all.py mySecretKey
   ```
   Files will now be generated in the plain folder.
   Decrypted files have `_plain` appended to their name.


## Clearing

Run the provided clear scripts to empty the cipher or plain directories.

