from django.test import TestCase

# Create your tests here.


def a(context):
    list = []
    for i in context:
        try:
            id = i['id']
            print(id)
        except Exception as e:
            print(e)
            return
        list.append(i)
    return list


def b():
    data = [{'id':'1'},{'id':'2'},{'s':'3'}]
    res = a(data)
    print(res)






