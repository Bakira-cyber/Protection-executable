import tkinter
import os
# import ask_key
import check


class c_key:
    def __init__(self, master, path):
        if os.path.exists(path):
            self.frame = tkinter.Frame(master, bd=70)
            self.text = tkinter.StringVar()
            L1 = tkinter.Label(self.frame, textvariable=self.text)
            app = check.check_key(path, self.frame, self.text)
            L1.pack()
            self.frame.pack()
