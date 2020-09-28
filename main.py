import tkinter
import true_key
import threads
import file_gui
import platform

# print(platform.uname())
win = tkinter.Tk()
win.title("Chemin pour les fichiers")
app = file_gui.gui(win)
win.mainloop()

# check=threads.DetectDBG()
# check.run()
# win = tkinter.Tk()
# win.configure(background='#9ac0e4')
# win.title("Vérifier la clé produit")
# app = true_key.c_key(win)
# win.geometry("300x50")
# win.mainloop()
