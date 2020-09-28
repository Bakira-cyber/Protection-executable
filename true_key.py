import tkinter
import os
# import ask_key
import check


class c_key:
    def __init__(self, master, path):
        self.frame = tkinter.Frame(master)
        self.text = tkinter.StringVar()
        L1 = tkinter.Label(self.frame, textvariable=self.text)
        if os.path.exists(path):
            self.fr = tkinter.Toplevel()
            self.fr.configure(background='#9ac0e4')
            self.fr.title("Vérifier la clé produit")
            app = check.check_key(path, self.frame, self.text)
        L1.pack()
        self.frame.pack()
