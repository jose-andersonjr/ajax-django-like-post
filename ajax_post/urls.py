
from . import views 
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^likepost/$', views.likePost, name='likepost')
]