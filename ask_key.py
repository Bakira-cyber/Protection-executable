import tkinter
import check


class Application:
    def __init__(self, master, frame, txt):
        self.frame = tkinter.Frame(master)
        self.master = master
        self.inputkey = tkinter.StringVar()
        L1 = tkinter.Label(self.frame, text="We do not have a license key for the software"
                                            ", you have to enter the license key :")
        text = tkinter.Entry(self.frame, textvariable=self.inputkey, width=60)
        self.btn_open = tkinter.Button(self.frame, text='Open', command=lambda: self.btn_check(frame, txt))
        L1.pack(side=tkinter.TOP)
        text.pack()
        self.btn_open.pack(side=tkinter.BOTTOM)
        self.frame.pack()

    def btn_check(self, frame, L1):
        b = ""
        if self.inputkey.get() != "":
            b = check.check_key(self.inputkey.get(), frame, L1)
        if b is True:
            self.master.destroy()
