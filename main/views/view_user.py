#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

__author__ = 'weichao02'
from django.shortcuts import render_to_response
from ..forms import UserForm
from ..util.tools import get_md5, get_login_user, get_response, is_need_to_login
from ..settings import LOGIN_TIMEOUT
from ..models import User


def public_parameter(request):
    """
    每个函数都会调这个，往这里面写入user信息
    """
    uri = request.path
    if not is_need_to_login(uri):
        user = User.objects.all()[0]
    else:
        uname = request.COOKIES.get('uname', request.POST.get('user_name', ''))
        user_list = User.objects.filter(user_name=uname)
        if user_list:
            user = user_list[0]
        else:
            user = User(user_name='fake', password='fake', email_address='fake@xxx.com')
    return {'user': user}


def register_user(request):
    """
    针对用户的注册
    如果是GET请求, 则直接返回注册页面; 如果是POST请求, 则接收注册校验, 并生成注册用户
    """
    if request.method == 'GET':
        return render_to_response('main/register.html',
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.password = get_md5(request.POST['password'])
            new_user.save()
            response = HttpResponseRedirect('/')
            username = request.POST['user_name']
            response.set_cookie("lt", get_md5(username), LOGIN_TIMEOUT)
            response.set_cookie("uname", username, LOGIN_TIMEOUT)
            return response
        else:
            return HttpResponseRedirect('/user/reg-user/')


def login_user(request):
    """
    针对用户的登陆
    """
    if request.method == 'GET':
        param_list = []
        for key, val in request.GET.items():
            if key == 'next':
                continue
            param_list.append(key + "=" + val)
        param_str = ''
        if param_list:
            param_str = '&' + "&".join(param_list)
        next_url = request.GET.get('next', '') + param_str
        return render_to_response("main/login.html",
                                  {'next': next_url},
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = get_login_user(username, password)
        if not user:
            return HttpResponseRedirect('/user/login/')
        redirect_to = request.POST.get('next', '')
        if not redirect_to:
            redirect_to = '/'
        response = HttpResponseRedirect(redirect_to)
        response.set_cookie("lt", get_md5(username), LOGIN_TIMEOUT)
        response.set_cookie("uname", username, LOGIN_TIMEOUT)
        return response


def profile_user(request, user_id):
    """
    获取个人详细信息
    """
    user = User.objects.get(pk=user_id)
    return render_to_response("main/profile.html", {'detail_user': user},
                              context_instance=RequestContext(request),
                              )


def check_user_name(request, user_name):
    """
    用户注册时，给定一个user_name，判断此用户名是否已被注册
    """
    exists = User.objects.filter(user_name=user_name).exists()
    return HttpResponse(get_response(0, "ok", {'exist': exists}))

