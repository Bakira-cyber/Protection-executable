import tkinter
import controlValues
import threads
import file_gui
import antiDBG

if not antiDBG.isThereADebugger():
    controlValues.control_all()
    win = tkinter.Tk()
    win.title("Chemin pour les fichiers")
    app = file_gui.gui(win)
    win.mainloop()
else:
    exit(-1)
# check=threads.DetectDBG()
# check.run()
# win = tkinter.Tk()
# win.configure(background='#9ac0e4')
# win.title("Vérifier la clé produit")
# app = true_key.c_key(win)
# win.geometry("300x50")
# win.mainloop()
