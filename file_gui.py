import tkinter
from tkinter import filedialog
import signature
import true_key


class gui:
    def __init__(self):
        self.frame = tkinter.Frame(borderwidth=10)
        self.excel_file = tkinter.StringVar()
        self.sign_file = tkinter.StringVar()
        tkinter.Label.pack(tkinter.Label(self.frame, text="Enter the Excel file path"))
        tkinter.Entry.pack(
            tkinter.Entry(self.frame, textvariable=self.excel_file, width=70, state="readonly", exportselection=0))
        btn_open_excel = tkinter.Button(self.frame, text='Open the Excel', command=lambda: self.open_excel_button())
        btn_open_excel.pack()
        tkinter.Label.pack(tkinter.Label(self.frame, text="Enter the signature file path"))
        tkinter.Entry.pack(
            tkinter.Entry(self.frame, textvariable=self.sign_file, width=70, state="readonly", exportselection=0))
        btn_sign_excel = tkinter.Button(self.frame, text='Open the signature', command=lambda: self.open_sign_button())
        btn_sign_excel.pack()
        btn_valided = tkinter.Button(self.frame, text='Valid', command=lambda: self.bt_valid())
        btn_valided.pack()
        self.frame.pack()

    def open_excel_button(self):
        file_name = filedialog.askopenfile(mode='r', filetypes=[("Excel files", "*.xlsx")])
        if file_name is not None:
            try:
                self.excel_file.set(file_name.name)
            except Exception as e:
                print(e)

    def open_sign_button(self):
        file_name = filedialog.askopenfile(mode='r', filetypes=[("signature", "*")])
        if file_name is not None:
            try:
                self.sign_file.set(file_name.name)
            except Exception as e:
                print(e)

    def bt_valid(self):
        self.frame.after(5, lambda: self.valid())

    def valid(self):
        if signature.verify(self.excel_file.get(), self.sign_file.get()) is None:
            win = tkinter.Toplevel()
            win.configure(background='#9ac0e4')
            win.title("Vérifier la clé produit")
            app = true_key.c_key(win, self.excel_file.get())
            win.mainloop()
