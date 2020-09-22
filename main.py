import tkinter
import true_key

win = tkinter.Tk()
win.configure(background='#9ac0e4')
win.title("Vérifier la clé produit")
app = true_key.c_key(win)
win.geometry("300x50")
win.mainloop()
