import tkinter
from tkinter import filedialog


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
        self.frame.pack()

    def open_excel_button(self):
        file_name = filedialog.askopenfile(mode='r', filetypes=[("Excel files", "*.xlsx")])
        if file_name is not None:
            try:
                self.excel_file.set(file_name.name)
            except Exception as e:
                print(e)

    def open_sign_button(self):
        file_name = filedialog.askopenfile(mode='r', filetypes=[("signature", "*.txt")])
        if file_name is not None:
            try:
                self.sign_file.set(file_name.name)
            except Exception as e:
                print(e)

