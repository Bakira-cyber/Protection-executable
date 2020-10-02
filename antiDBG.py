# usefull tools :
# https://github.com/LordNoteworthy/al-khaser

# https://github.com/Arvanaghi/CheckPlease/blob/master/Python/detect_debugging.py

from ctypes import *


def isThereADebugger():
    # Detect if there is a debbuger scanning our program
    if windll.kernel32.IsDebuggerPresent():
        print("Error ! You are not allowed to debug the Program !")
        exit(-1)
    else:
        print("RSA")
        return 0
