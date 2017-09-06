# -*- coding:utf-8 -*-

from django.conf.urls import url,include
from todoApp import views

urlpatterns = [
    url(r'^$', views.todolist, name='todo'),
    url(r'^completed/$', views.completed, name='completed'),
    url(r'^addtodo/$', views.addtodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$',  views.todofinish, name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', views.todoback,   name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$',  views.updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$',  views.tododelete, name='delete'),
]
