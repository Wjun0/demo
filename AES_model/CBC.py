
from base64 import b64decode,b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class CBC_model():
    def __init__(self, key):
        self.key = pad(key.encode(), AES.block_size)
        self.aes = AES.new(key=self.key, mode=AES.MODE_CBC)

    def encrypt(self, data):
        # 加密
        b_data = self.aes.encrypt(pad(data.encode(), AES.block_size))
        iv = b64encode(self.aes.iv).decode()
        sign = b64encode(b_data).decode()
        print(f"CBC模式加密结果：")
        print("iv:", iv)
        print("c_text:", sign)
        return iv, sign

    def decrypt(self,iv,sign):
        #解密
        try:
            iv = b64decode(iv)
            sign = b64decode(sign)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(sign), AES.block_size).decode()
            print("CBC模式解密结果：", pt)
            return pt
        except Exception as e:
            print(e)


if __name__ == '__main__':
    ecb = CBC_model(key = "12324ddfdafd")
    iv, sign = ecb.encrypt(str({"test": "123456"}))
    ecb.decrypt(iv, sign)

    # CBC模式加密结果：
    # iv: qpdBrlZiW/2z4kKxQ06Pgg==
    # c_text: wGmv7ckAPv/DvM/otNtn4+f7ZZ27Pf/2GFuKexFJPlY=

    # CBC模式解密结果： {'test': '123456'}