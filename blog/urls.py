from django.conf.urls import url
from blog.views import post_list 
from blog.views import post_detail


from django.contrib import admin
from . import views

 

urlpatterns = [
        url(r'^$',post_list,name='blog'),
        url(r'^(?P<id>\d+)/$', post_detail, name='view_post'),
        url(r'^post/new/$', views.new_post, name='new_post'),
        url(r'^(?P<id>\d+)/edit$', views.edit_post),
]
