from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getquerystring(request):
    '''
    演示接收查询字符串参数
    :param request:
    :return:
    '''
    # 获取查询字符串参数:
    querydict = request.GET
    a = querydict.get('a')
    blist = querydict.getlist('b')

    # 打印:
    print(a)
    print(blist)

    return HttpResponse('getquerystring')