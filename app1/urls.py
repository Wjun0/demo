from django.conf.urls import url
from . import views, xhtml2pdf

urlpatterns = [
    url(r'^getquerystring/$', views.getquerystring),
    url('^students/$',views.Student_index.as_view()),
    url(r'emp/$',views.EmpAPI.as_view()),
    url(r'^upload/$',views.upload),
    url(r'^render_pdf/$', xhtml2pdf.render_pdf_view),
]