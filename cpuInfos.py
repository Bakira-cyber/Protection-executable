from cpuinfo import get_cpu_info
import tkinter as tk
import hashlib 
import json 

def show_info():

    root=tk.Tk()
    sign_file = tk.StringVar()

    info = get_cpu_info()

    info = json.dumps(info)

    hash_info = hashlib.sha256(info.encode('utf-8')).hexdigest()

    sign_file.set(hash_info)

    """
    info.encode('utf-8')
    
    hash_info = hashlib.sha256()
    hash_info.update(info)
    hash_info.hexdigest
    """
    print("Hash of the CPU's infos")

    root.title("Protection des Exécutables")

    
    #tk.Label(root, text=hash_info).pack()
    tk.Entry.pack(tk.Entry(root, textvariable=sign_file, width=0.7, state="readonly", exportselection=0))
    tk.Button(root, text="ok", command=root.destroy).pack()

    root.mainloop()




if __name__ == '__main__':
    show_info()
    
