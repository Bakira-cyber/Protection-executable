import random
import sys, os
import tkinter
from threading import Thread
import time
import file_gui
import antiDBG
import controlValues


class DetectDBG(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run_deb(self):
            sys.stdout.write("Analyse")
            sys.stdout.flush()

            antiDBG.isThereADebugger()


    def run_gui(self):
        print(1)

"""
usefull links : 
https://note.nkmk.me/en/python-script-file-path/

"""
