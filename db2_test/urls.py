from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$',views.user),
    url(r'^userslist/$',views.UserList.as_view()),
    url(r'^userslist/(?P<pk>\d+)/$',views.UserRetrive.as_view()),
    url(r'^us/(?P<pk>\d+)/$',views.UserUpdate.as_view()),
    url(r'^update/$', views.Update_db2_user.as_view()),
]