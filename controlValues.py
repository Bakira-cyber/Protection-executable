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


"""
def controlValues(path):
    with open(path, 'rb') as f:
        code = f.read()
        hashlib.sha256().update(code)
        print(path, hashlib.sha256().hexdigest())
        return hashlib.sha256().hexdigest()
"""
"""
def controlValues():
    with open(os.path.dirname(sys.argv[0]), 'rb') as f:
        code = f.read()
        hashlib.sha256().update(code)
        print(os.path.dirname(sys.argv[0]), hashlib.sha256().hexdigest())
        return hashlib.sha256().hexdigest()
"""