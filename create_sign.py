from OpenSSL import crypto
import base64


def sign():
    with open('Licence.txt', "r") as f:
        data = f.read()
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
    with open("signature", "wb") as f:
        f.write(data_base64)


# def sign():
#     df = pd.read_excel('Licence.xlsx')
#     data = df.to_string()
#     key_file = open("key.pem", "r")
#     key = key_file.read()
#     key_file.close()
#     if key.startswith('-----BEGIN '):
#         pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
#     else:
#         raise PermissionError
#     data = data.encode()
#     sign = crypto.sign(pkey, data, "sha256")
#     data_base64 = base64.b64encode(sign)
#     with open("signature", "wb") as f:
#         f.write(data_base64)

sign()
