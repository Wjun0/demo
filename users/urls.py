from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='indexname'),
    url(r'^say/$', views.say),
    url(r'^say1/$', views.say1),
    url(r'^say2/$', views.say2),
    url(r'^say3/$', views.say3),
    url(r'^sayhello/$', views.sayhello, name='sayname'),
    url(r'^test/$',views.test),
    url(r'^excel_export',views.excel_export), #导出excel
    url(r'^xss_test/$',views.xss_f),

]