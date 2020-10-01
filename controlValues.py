# Import hashlib library (SHA256 method is part of it)
import hashlib
import sys, os

# Import ConfigParser to easily access control values
import configparser

config = configparser.ConfigParser()
config.read('Values.ini')

original_main_controlvalue = config['ControlValues']['original_main_controlvalue']
original_threads_controlvalue = config['ControlValues']['original_threads_controlvalue']
original_antiDBG_controlvalue = config['ControlValues']['original_antiDBG_controlvalue']
original_control_controlvalue = config['ControlValues']['original_control_controlvalue']
original_check_controlValue = config['ControlValues']['original_check_controlValue']
original_true_controlValue = config['ControlValues']['original_true_controlValue']
original_file_gui_controlValue = config['ControlValues']['original_file_gui_controlValue']

def controlvalues_main():
    with open("main.py") as main_file:
        data = main_file.read()
    returned_main_controlvalue = hashlib.sha256(data).hexdigest()

    if original_main_controlvalue != returned_main_controlvalue:
        exit(-1)


def controlvalues_threads():
    with open("threads.py") as threads_file:
        data = threads_file.read()
    returned_threads_controlvalue = hashlib.sha256(data).hexdigest()

    if original_threads_controlvalue != returned_threads_controlvalue:
        exit(-1)


def controlvalues_antiDBG():
    with open("antiDBG.py") as antiDBG_file:
        data = antiDBG_file.read()
        returned_antiDBG_controlvalue = hashlib.sha256(data).hexdigest()

    if original_antiDBG_controlvalue != returned_antiDBG_controlvalue:
        exit(-1)


def controlvalues_control():
    with open("controlValues.py") as control_file:
        data = control_file.read()
        returned_control_controlvalue = hashlib.sha256(data).hexdigest()

    if original_control_controlvalue != returned_control_controlvalue:
        exit(-1)


def controlvalues_check():
    with open("check.py", 'rb') as check:
        data = check.read()
    returned_controlvalue = hashlib.sha256(data).hexdigest()
    if original_check_controlValue != returned_controlvalue:
        exit(-1)


def controlvalues_true():
    with open("true_key.py", 'rb') as check:
        data = check.read()
    returned_controlvalue = hashlib.sha256(data).hexdigest()
    if original_true_controlValue != returned_controlvalue:
        exit(-1)


def controlvalues_file_gui():
    with open("file_gui.py", 'rb') as check:
        data = check.read()
    returned_controlvalue = hashlib.sha256(data).hexdigest()
    if original_file_gui_controlValue != returned_controlvalue:
        exit(-1)


def controlValues(path):
    with open(path, 'rb') as f:
        code = f.read()
        print(code)
        hash_code = hashlib.sha256(code).hexdigest()
        print(path, hash_code)
        return hash_code


controlValues("file_gui.py")
controlvalues_file_gui()

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
