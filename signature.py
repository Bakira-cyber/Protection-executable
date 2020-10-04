from tkinter import messagebox
from OpenSSL import crypto
import base64


def verify(path, path_sign):
    with open(path, "r") as f:
        data = f.read()
    key_file = open("public.pem", "r")
    key = key_file.read()
    key_file.close()
    if key.startswith('-----BEGIN '):
        pkey = crypto.load_publickey(crypto.FILETYPE_PEM, key)
    else:
        raise PermissionError
    data = data.encode()
    x509 = crypto.X509()
    x509.set_pubkey(pkey)
    with open(path_sign, "rb") as f:
        signature = f.read()
    signature = base64.b64decode(signature)
    try:
        return crypto.verify(x509, signature, data, "sha256")
    except:
        messagebox.showerror(title="Signature error", message="Your signature is not corresponding to the licence file")

# def verify(path, path_sign):
#     df = pd.read_excel(path)
#     data = df.to_string()
#     key_file = open("public.pem", "r")
#     key = key_file.read()
#     key_file.close()
#     if key.startswith('-----BEGIN '):
#         pkey = crypto.load_publickey(crypto.FILETYPE_PEM, key)
#     else:
#         raise PermissionError
#     data = data.encode()
#     x509 = crypto.X509()
#     x509.set_pubkey(pkey)
#     with open(path_sign, "rb") as f:
#         signature = f.read()
#     signature = base64.b64decode(signature)
#     return crypto.verify(x509, signature, data, "sha256")
