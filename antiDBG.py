# usefull tools :
# https://github.com/LordNoteworthy/al-khaser

# https://github.com/Arvanaghi/CheckPlease/blob/master/Python/detect_debugging.py

from ctypes import *

isDebuggerPresent = windll.kernel32.IsDebuggerPresent()


def isDebbugerPresent():
    # Detect if there is a debbuger scanning our program
    if isDebuggerPresent():
        print("Error ! You are not allowed to debug the Program !")
        exit(-1)
    return 0
