# Import hashlib library (SHA256 method is part of it)
import hashlib
import sys


def controlValues(path):
    with open(path, 'rb') as f:
        code = f.read()
        hashlib.sha256().update(code)
        print(path, hashlib.sha256().hexdigest())
        return hashlib.sha256().hexdigest()


"""
def controlValues(file_name):
    
    # File to check
    #file_name = 'file.py'

    # Correct original SHA256 goes here
    original_sha256 = '5d41402abc4b2a76b9719d911017c592'   #need to verify with the final code, page by page  

    # Open,close, read file and calculate SHA256 on its contents 
    with open(file_name) as file_to_check:
        # read contents of the file
        data = file_to_check.read()    
        # pipe contents of the file through
        sha256_returned = hashlib.sha256(data).hexdigest()

    # Finally compare original SHA256 with freshly calculated
    if original_sha256 == sha256_returned:
        print("checksum verified.")

    else:
        print("checksum verification failed!.")
        sys.exit(0)
"""
