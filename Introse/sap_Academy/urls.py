from django.conf.urls import url
from . import views

app_name = 'sapApp'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^students/$', views.students, name='students'),
    url(r'^grades/$', views.grades, name='grades'),
    url(r'^grades2/$', views.grades2, name='grades2'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
]