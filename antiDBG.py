# usefull tools :
# https://github.com/LordNoteworthy/al-khaser

# https://github.com/Arvanaghi/CheckPlease/blob/master/Python/detect_debugging.py
import inspect


def isThereADebugger():
    # Detect if there is a debbuger scanning our program
    for frame in inspect.stack():
        if frame[1].endswith("pydevd.py"):
            return True
    return False
