import itsdangerous

salt = 'paZu2nSjlBTzkUam6Bd8'  # 加盐
t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=600)  # 过期时间600秒



def it_encode(data):
    # =========加密token============
    res = t.dumps(data)
    token = res.decode()  # 指定编码格式
    print(token)
    return token


def it_decode(token):
    res = t.loads(token)
    print(res)
    # {'username': 'baihe', 'user_id': 1}
    return res

if __name__ == '__main__':
    # t_token = "eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJleHAiOjE2Njc3MDA1NjZ9.TFvwzlps4JQGpP9lb9Llk_THhgCM6Po-i7fHgCT-8N0"
    # it_decode(t_token)

    data = {"username": "testtest1", "password": "test123456", "exp": 1667700566}
    token = it_encode(data)

    it_decode(token)
    from simpleleader import PeerLeader