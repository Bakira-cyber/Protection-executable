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
    signature = crypto.sign(pkey, data, "sha256")
    data_base64 = base64.b64encode(signature)
    print(data_base64)

    with open("signature.txt", "w") as f:
        f.write(signature)
