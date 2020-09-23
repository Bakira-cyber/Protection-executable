from OpenSSL import crypto
import base64
import pandas as pd


def gen():
    # OpenSSL.crypto.PKey().generate_key(crypto.TYPE_RSA, 256)
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 1024)
    print(key)


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


def verify(signature):
    df = pd.read_excel(r'D:\Python projects\Software protection\Licence.xlsx')
    data = df.to_string()
    key_file = open("public.pem", "r")
    key = key_file.read()
    key_file.close()
    print(key)
    if key.startswith('-----BEGIN '):
        pkey = crypto.load_publickey(crypto.FILETYPE_PEM, key)
    else:
        raise PermissionError
    print(pkey)
    data = data.encode()
    x509 = crypto.X509()
    x509.set_pubkey(pkey)
    return crypto.verify(x509, signature, data, "sha256")


# signature = sign()

# print(verify(signature))

code = compile("print('hello world')", '<string>', 'eval')
exec(code)
