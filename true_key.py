import tkinter
import os
import ask_key


class c_key:
    def __init__(self, master):
        self.frame = tkinter.Frame(master)
        self.text = tkinter.StringVar()
        L1 = tkinter.Label(self.frame, textvariable=self.text)
        if os.path.exists("Licence.xlsx"):
            self.fr = tkinter.Toplevel()
            self.fr.configure(background='#9ac0e4')
            self.fr.title("Vérifier la clé produit")
            app = ask_key.Application(self.fr, self.frame, self.text)
        L1.pack()
        self.frame.pack()
