# -*- coding:utf-8 -*-



from django.shortcuts import render
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from todoApp.models import Todo
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

'''
todolist view模块 主要处理以下页面：
1 主页面 主页面显示当前代办事项 todolist
2 完成页面 显示已经完成的事项 completed
3 添加事项页面 addtodo
'''


# Create your views here.
def todolist(request):
    todolist = Todo.objects.filter(flag=1)
    # finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpleTodo.html',
                              {'todolist': todolist},
                              RequestContext(request))
def completed(request):
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpleTodo.html',
                              {'finishtodos': finishtodos},
                              RequestContext(request))


def todofinish(request, id=""):
    todo = Todo.objects.get(id=id)
    if todo.flag == "1":
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpleTodo.html',
                              {'todolist': todolist, 'finishtodos': finishtodos},
                              RequestContext(request))


def todoback(request, id=""):
    todo = Todo.objects.get(id=id)
    if todo.flag == '0':
        todo.flag = 1
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpleTodo.html',
                              {'todolist': todolist, 'finishtodos': finishtodos},
                              RequestContext(request))


def tododelete(request, id=""):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('simpleTodo.html',
                              {'todolist': todolist, 'finishtodos': finishtodos},
                              RequestContext(request))

@csrf_exempt
def addtodo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        return HttpResponseRedirect('/')
    else:
        return render_to_response('addtodo.html', RequestContext(request))







@csrf_exempt
def updatetodo(request, id=''):
    if request.method == 'POST':
        print('ddd')
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        try:
            todo = Todo.objects.get(id=id)
            # todo = Todo.objects.get(id=37)
        except Exception:
            raise Http404
    return render_to_response('updatetodo.html', {'todo': todo}, RequestContext(request))




