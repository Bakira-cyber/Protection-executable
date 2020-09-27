from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import base64


# Cypher program
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# https://nitratine.net/blog/post/encryption-and-decryption-in-python/

# Protect binary executable :
# https://www.embedded.com/protecting-binary-executables/

def generate_key():
    password_provided = "password"  # This is input in the form of a string
    password = password_provided.encode()  # Convert to type bytes
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once


def encrypt_program():
    key = b''
    input_file = 'test.py'
    output_file = 'test.encrypted'

    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the input file

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)  # Write the encrypted bytes to the output file


def decrypt_program():
    key = b''
    input_file = 'test.encrypted'
    output_file = 'test.txt'

    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)  # Write the decrypted bytes to the output file

    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")
