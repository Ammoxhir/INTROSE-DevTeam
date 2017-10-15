from django.conf.urls import url
from .import views

app_name = 'sapApp'

urlpatterns= [
    url(r'^$', views.tryLogin, name='tryLogin'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^students/$', views.students, name='students'),
    url(r'^students2/(?P<sapID>[0-9]+)$', views.students2, name='students2'),
    url(r'^grades/$', views.grades, name='grades'),
    url(r'^grades2/$', views.grades2, name='grades2'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^specificreport/$', views.reports, name='specificreport'),
    url(r'^login/$', views.login, name='login'),
    url(r'^sortIt/$', views.sortIt, name='sortIt'),
    url(r'^userprofile/$', views.userprofile, name='userprofile'),
    url(r'^signup/$', views.signup, name='signup'),
]



