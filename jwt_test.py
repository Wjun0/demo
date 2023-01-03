import time
import jwt

headers = {"typ":"jwt","alg":"HS256"}
secrect = "e10adc3949ba59abbe56e057f20f883e"


def jwt_decode(token):
    data = None
    try:
        data = jwt.decode(token, secrect, algorithms=['HS256'],headers=headers)
    except Exception as e:
        print(e)
    print(data)
    return data

def jwt_encode(data):
    jwt_token = jwt.encode(data, secrect, algorithm='HS256',headers=headers).decode('ascii')
    print(jwt_token)
    return jwt_token


if __name__ == '__main__':
    t_token = "eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJleHAiOjE2Njc3MTcyNzB9.FXvX8e9wS2WgiDjGGriNTx4CVM2OUTKbXPGbaHPlQFc"
    jwt_decode(t_token)

    data = {"username":"admin","password":"1234567","exp":1667717270}
    token = jwt_encode(data)

    jwt_decode(token)

