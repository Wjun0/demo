from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='indexname'),
    url(r'^say/$', views.say),
    url(r'^sayhello/$', views.sayhello, name='sayname'),
    url(r'^test/$',views.test),

]