import time

from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse


# Create your views here.
from django.urls import reverse

from django.db import close_old_connections

from users import urls
from users.models import Student

from django.conf.urls import url,include
# from arya.service.sites import site
from django.urls.resolvers import RegexURLPattern
from django.urls.resolvers import RegexURLResolver
from django.shortcuts import HttpResponse




def say(request):
    print('say')
    time.sleep(500)
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


def index(request):
    from demo.urls import urlpatterns
    print(get_all_url(urlpatterns, prev='/'))
    return HttpResponse('hello django')


def get_all_url(urlparrentens,prev,is_first=False,result=[]):

    for item in urlparrentens:
        v = item._regex.strip('^$')#去掉url中的^和$
        if isinstance(item,RegexURLPattern):
            result.append(prev + v)

        # 处理总路由为：url(r'^', include('requresp.urls') 形式的
        elif isinstance(item, RegexURLResolver):
            dic = item.reverse_dict.values()
            for i in dic:
                print(i[1])
                result.append(item._regex + i[1])
    print(result)
    res = []
    for item in result:
        res.append(item.strip('^$'))
    return res
