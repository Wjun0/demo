from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getquerystring/$', views.getquerystring),
    url('^students/$',views.Student_index.as_view()),
]