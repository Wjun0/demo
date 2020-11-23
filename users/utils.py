import redis
pool = redis.ConnectionPool(host='192.168.59.129',port=6379,db=15)
redis_db = redis.StrictRedis(connection_pool=pool)



if __name__ == '__main__':
    redis_db.set('key',12)
    print('save ok')
    id = redis_db.get('key')

    print(id)
    redis_db.set('key',15)
    print(redis_db.get('key').decode())