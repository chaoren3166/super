#-*- coding: utf-8 -*-
from twisted.python.hashlib import md5
from ..models import LoginFree, User
import json

__author__ = 'weichao02'


def get_md5(content):
    """
    获取内容md5加密后的值
    """
    m = md5()
    m.update(content)
    return m.hexdigest()


def get_param_string(request):
    """
    获取http头中的get字符串
    """
    result_dict = []
    for key, val in request.GET.items():
        result_dict.append(key + '=' + val)
    if not result_dict:
        return ''
    return "&".join(result_dict)


def is_need_to_login(uri):
    """
    给定一个uri, 判断是否需要先登陆
    """
    all_result = LoginFree.objects.all()
    if not all_result:
        return True
    for sin_obj in all_result:
        path_prefix = sin_obj.path_prefix
        if uri.startswith(path_prefix):
            return False
    return True


def is_logined_in(request):
    """
    通过cookie判断用户是否已经登录
    """
    cookies = request.COOKIES
    if 'lt' in cookies and 'uname' in cookies:
        lt = cookies['lt']
        uname = cookies['uname']
        if lt == get_md5(uname):
            user = User.objects.filter(user_name=uname)
            return user[0]
    return False


def get_login_user(user_name, password):
    """
    登陆认证
    """
    user_md5 = get_md5(password)
    user = User.objects.filter(user_name=user_name, password=user_md5)
    if user:
        return user[0]
    return None


def get_response(code, msg, dic):
    """
    根据code, msg, dic获取json字串
    """
    return json.dumps({'code': code, 'msg': msg, 'data': dic})


def get_next_auto_id(table_name):
    """
    对于一个有自增Id的表, 获取此表的下一个自增id的值
    """
    sql = 'SELECT AUTO_INCREMENT next_id FROM information_schema.TABLES ' \
          'WHERE TABLE_SCHEMA = "super" AND TABLE_NAME = "%s"' % table_name
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    return row[0]
