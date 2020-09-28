from cpuinfo import get_cpu_info
import tkinter as tk
import hashlib
import json


def show_info(top):
    frame = tk.Frame(master=top, borderwidth=10)
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

    # frame.title("Protection des Exécutables")

    # tk.Label(root, text=hash_info).pack()
    tk.Entry.pack(tk.Entry(frame, textvariable=sign_file, width=65, state="readonly"))
    tk.Button(frame, text="ok", command=frame.destroy).pack()

    frame.pack()
