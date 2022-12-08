from base64 import b64decode,b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class ECB_model():
    def __init__(self, key):
        self.key = pad(key.encode(), AES.block_size, style="pkcs7")
        self.aes = AES.new(key=self.key, mode=AES.MODE_ECB)

    def encrypt(self, data):
        # 加密
        b_data = self.aes.encrypt(pad(data.encode(), AES.block_size))
        sign = b64encode(b_data).decode()
        print("ECB模式加密结果：", sign)
        return sign

    def decrypt(self,sign):
        #解密
        b_data = b64decode(sign)
        data = unpad(self.aes.decrypt(b_data), AES.block_size).decode()
        print("ECB模式解密结果：", data)
        return data


if __name__ == '__main__':
    ecb = ECB_model(key = "12324dfd")
    ecb.decrypt(ecb.encrypt(str({"test":"123456"})))

    # ECB模式加密结果： uNc/QUv5FOkm9JUfjMr3T0VyTZ9d6TJRHxa6KoaBIMI=
    # ECB模式解密结果： {'test': '123456'}