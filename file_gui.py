import tkinter


class gui:
    def __init__(self):
        self.frame = tkinter.Frame()
        self.excel_file = tkinter.StringVar()
        self.sign_file = tkinter.StringVar()
        tkinter.Label.pack(tkinter.Label(self.frame, text="Enter the Excel file path", bg="#9ac0e4"))
        btn_open_excel = tkinter.Button(self.frame, text='Open', command=lambda: self.open_excel_button())
        btn_open_excel.pack()
        tkinter.Entry.pack(
            tkinter.Entry(self.frame, textvariable=self.excel_file, width=25, state="readonly", bg="#9ac0e4",
                          exportselection=0))
        tkinter.Label.pack(tkinter.Label(self.frame, text="Enter the signature file path", bg="#9ac0e4"))
        btn_sign_excel = tkinter.Button(self.frame, text='Open', command=lambda: self.open_sign_button())
        btn_sign_excel.pack()
        tkinter.Entry.pack(
            tkinter.Entry(self.frame, textvariable=self.sign_file, width=25, state="readonly", bg="#9ac0e4",
                          exportselection=0))

