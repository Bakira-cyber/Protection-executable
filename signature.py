from OpenSSL import crypto
import base64
import pandas as pd


def sign():
    df = pd.read_excel(r'D:\Python projects\Software protection\Licence.xlsx')
    data = df.to_string()
    key_file = open("key.pem", "r")
    key = key_file.read()
    key_file.close()
    if key.startswith('-----BEGIN '):
        pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
    else:
        raise PermissionError
    data = data.encode()
    sign = crypto.sign(pkey, data, "sha256")
    data_base64 = base64.b64encode(sign)
    print(data_base64)
    return sign


def verify(path, path_sign):
    df = pd.read_excel(path)
    data = df.to_string()
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
        print(signature)
    signature = base64.b64decode(signature)
    return crypto.verify(x509, signature, data, "sha256")

sign()
verify("Licence.xlsx","sign")