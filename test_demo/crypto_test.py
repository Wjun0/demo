import ast
from base64 import b64encode
from Crypto.Util.Padding import pad
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# key只能传入bytes
key = 'ssssssssssfsssssssssssssssfsssss'.encode()

def pad_key(key):  # 限制只能传入长度为16，32
    while len(key) % 16 != 0:
        key += b' '     #不足的用空格补全
    return key

def get_sign(data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    print(iv)
    print(ct)
    return iv,ct    # 返回偏移和加密数据


def de_sign(iv, sign):
    iv = b64decode(iv)
    ct = b64decode(sign)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return ast.literal_eval(str(pt, encoding='utf-8'))


if __name__ == '__main__':
    data = str({'name':'xxx','um':"xxx"}).encode()
    iv,sign = get_sign(data)
    data = de_sign(iv,sign)
    print(data)

# '{"iv": "bWRHdzkzVDFJbWNBY0EwSmQ1UXFuQT09", "ciphertext": "VDdxQVo3TFFCbXIzcGpYa1lJbFFZQT09"}'
# from Crypto.Cipher import AES
#
# key = 'ACD310AE179CE245624BB238867CE189'
# message = 'this is my super secret message'
#
# cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
#
# def pad(s):
#     return s + ((16 - len(s) % 16) * '{')
#
# def encrypt(plaintext):
#     global cipher
#     return cipher.encrypt(pad(plaintext).encode('utf-8'))
#
# def decrypt(ciphertext):
#     global cipher
#     dec = cipher.decrypt(ciphertext).decode('utf-8')
#     l = dec.count('{')
#     return dec[:len(dec) - 1]
#
# encrypted = encrypt(message)
# decrypted = decrypt(encrypted)
#
# print("Message: ", message)
# print("Encrypted: ", encrypted)
# print("Decrypted: ", decrypted)
#

# from Crypto.Cipher import AES
# 
# key = b'Sixteen byte key'
# data = b'hello from other side'
# 
# e_cipher = AES.new(key, AES.MODE_EAX)
# e_data = e_cipher.encrypt(data)
# 
# d_cipher = AES.new(key, AES.MODE_EAX, e_cipher.nonce)
# d_data = d_cipher.decrypt(e_data)
# 
# print("Encryption was: ", e_data)
# print("Original Message was: ", d_data)