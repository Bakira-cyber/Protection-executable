from cpuinfo import get_cpu_info
import tkinter as tk
import hashlib
import json


def get_info():
    info = get_cpu_info()
    info = json.dumps(info)
    return hashlib.sha256(info.encode('utf-8')).hexdigest()


def show_info(top):
    frame = tk.Frame(master=top, borderwidth=10)
    sign_file = tk.StringVar()

    sign_file.set(get_info())

    """
    info.encode('utf-8')
    
    hash_info = hashlib.sha256()
    hash_info.update(info)
    hash_info.hexdigest
    """

    tk.Entry.pack(tk.Entry(frame, textvariable=sign_file, width=65, state="readonly"))
    tk.Button(frame, text="Close", command=top.destroy).pack()

    frame.pack()
