from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse


# Create your views here.
from django.urls import reverse


def index(request):
    '''
    索引的视图函数: 接口
    :param request:
    :return:
    '''
    print('index')

    # result = 1 / 0

    return HttpResponse('hello django')


def say(request):
    print('say')
    return HttpResponse('say')


def sayhello(request):
    print('sayhello')

    # reverse('namespace:name')
    # url = reverse('username:sayname')
    # print(url)

    url = reverse('username:indexname')
    print(url)

    return redirect(url)


from .utils import redis_db
def test(request):
    import pymysql
    try:
        conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='mysql',
            db = 'sql_test'
            )
        cur=conn.cursor()

        # id = redis_db.get('key2')
        # if not id:
        #     id = 0
        # else:
        #     id = id.decode()

        sql = 'select * from emp where empid > {}'.format(1)
        cur.execute(sql)
        data = cur.fetchall()
        res = []
        for d in data:
            print(d)
            res.append(list(d))

        print(type(data))
        cur.close()

        res_dic = []
        key_list = []
        for i in data:
            if i[3] not in key_list:
                dic= {}
                dic['name'] = i[3]
                dic['name__count'] = 1
                res_dic.append(dic)
                key_list.append(i[3])
            else:
                for j in res_dic:
                    if j.get('name') == i[3]:
                        j['name__count'] = j.get('name__count') + 1
        print(res_dic)




        print(res_dic)

        if not data:
            return HttpResponse([])

        # else:
        #     id = list(data)[-1][0]
        #     redis_db.set('key2',id)
        #     print(id)

    except Exception as e:
        print(e)
        return HttpResponse(e,status=500)
    print(res)
    print(type(res))
    return JsonResponse(res,safe=False)