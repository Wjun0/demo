import binascii
from io import StringIO

from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse


# Create your views here.
from django.urls import reverse

from django.db import close_old_connections
from rest_framework.response import Response
from rest_framework.views import APIView

from users import urls
from users.models import Student, Emp

from django.conf.urls import url,include
# from arya.service.sites import site
from django.urls.resolvers import RegexURLPattern
from django.urls.resolvers import RegexURLResolver
from django.shortcuts import HttpResponse
import os
from xlwt import *



def xss_f(request):
    text = request.GET.get('id')

    ###### 对抗xss ######
    from django.utils.html import strip_tags
    text = strip_tags(text)
    #############

    html = """
    <html>
        <body>
            xxx
            <h1 >

            </h1>
        </body> 
        {}
    </html>
    """.format(text)
    # < script > alert("xss 执行") < / script >
    # <script>alert("xss")</script>
    return HttpResponse(html)
    # return render(request,"index.html",context={"text":text})


def excel_export(request):
    """
    导出excel表格
    """
    list_obj = Student.objects.all()
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"学生表")
        w.write(0, 0, "学号")
        w.write(0, 1, u"姓名")
        w.write(0, 2, u"性别")
        w.write(0, 3, u"出生日期")
        # 写入数据
        excel_row = 1
        for obj in list_obj:
            data_id = obj.sno
            data_user = obj.sname
            data_sex = obj.ssex
            data_birthday = obj.sbirthday.strftime("%Y-%m-%d")
            # obj.sbirthday.strftime("%Y-%m-%d")
            w.write(excel_row, 0, data_id)
            w.write(excel_row, 1, data_user)
            w.write(excel_row, 2, data_sex)
            w.write(excel_row, 3, data_birthday)
            excel_row += 1
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test.xls")
        if exist_file:
            os.remove(r"test.xls")
        ws.save("test.xls")
        ############################
        import io
        output = io.BytesIO()
        ws.save(output)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test.xls'
        response.write(output.getvalue())
        return response


def say(request):
    print('say')
    stus = Student.objects.all()
    for i in stus:
        print(i)
    return HttpResponse('say')

def say1(request):
    print('say')
    stus = Student.objects.all()
    for i in stus:
        print(i)
    return HttpResponse('say')
def say2(request):
    print('say')
    stus = Student.objects.all()
    for i in stus:
        print(i)
    return HttpResponse('say')
def say3(request):
    print('say')
    stus = Student.objects.all()
    for i in stus:
        print(i)
    return HttpResponse('say')

def sayhello(request):
    print('sayhello')
    stus = Student.objects.all()
    for i in stus:
        print(i)

    print(1)
    emp = Emp.objects.all()
    for i in emp:
        print(i.name)

    print(2)
    emp = Emp.objects.filter(deptno="01")
    for i in emp:
        print(i)

    # reverse('namespace:name')
    # url = reverse('username:sayname')
    # print(url)

    # url = reverse('username:indexname')
    # print(url)
    # return redirect()
    return HttpResponse([])

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
