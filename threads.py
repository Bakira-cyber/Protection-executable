import random
import sys, os
from threading import Thread
import time
import file_gui
import antiDBG
import controlValues


class DetectDBG(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            sys.stdout.write("Analyse")
            sys.stdout.flush()

            antiDBG.isThereADebugger()

            attente = 10
            time.sleep(attente)


"""
usefull links : 
https://note.nkmk.me/en/python-script-file-path/

"""
