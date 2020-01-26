from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.kirim_list, name='kirim_list'),
    url(r'^kirim/(?P<pk>\d+)/$', views.kirim_detail, name='kirim_detail'),
    url(r'^kirim/new/$', views.kirim_new, name='kirim_new'),
    url(r'^kirim/(?P<pk>\d+)/edit/$', views.kirim_edit, name='kirim_edit'),
] 