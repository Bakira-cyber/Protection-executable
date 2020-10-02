import tkinter
import os

from PIL import ImageTk,Image

import check
import controlValues


class c_key:
    def __init__(self, master, path):
        # controlValues.controlvalues_check()
        if os.path.exists(path):
            self.canvas = tkinter.Canvas(master, width=300, height=300)
            self.img = ImageTk.PhotoImage(Image.open("4b5aef2232fd494af215f853d5e29e20UAjyjTp5NXCNbgql-22.jpeg"))
            self.canvas.create_image(20, 20, anchor=tkinter.NW, image=self.img)
            # self.frame = tkinter.Frame(master, bd=70)
            self.text = tkinter.StringVar()
            app = check.check_key(path, self.canvas, self.text, master)
