#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ..forms import UploadFileForm
from ..models import UserImage, User
import os
from ..util.tools import get_next_auto_id
from ..util.file_util import get_extension_name, create_thumbnails
from ..service.album_service import get_mine_image_list
import datetime

__author__ = 'weichao02'


def render_main_page(request):
    """
    跳转至默认页
    """
    return render_to_response("main/home.html",
                              context_instance=RequestContext(request))


def show_mine_albums(request, user_id):
    """
    展示我的图片列表
    """
    image_list = get_mine_image_list(user_id, 0)
    return render_to_response("album/mine.html",
                              {'menu_active': 'my-album', 'image_list': image_list},
                              context_instance=RequestContext(request))


def show_friend_albums(request):
    return render_to_response("album/friends.html",
                              {'menu_active': 'friend-album'},
                              context_instance=RequestContext(request))


def upload_pic(request):
    """
    上传图片
    """
    if request.method == 'GET':
        return render_to_response("album/upload.html",
                                  {'menu_active': 'upload-pic'},
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        if not request.POST['title']:
            request.POST['title'] = "无描述"
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_upload_file(request)
            return HttpResponseRedirect('/album/mine/' + request.POST['user_id'] + '/')
        else:
            return HttpResponseRedirect('/album/upload/')


def save_upload_file(request):
    """
    保存大图和小图
    """
    #获取user信息
    user = User.objects.get(pk=long(request.POST['user_id']))
    if not user:
        return
    user_id = user.id
    f = request.FILES['my_img']

    #获取保存的名称
    image_id = get_next_auto_id('user_image')
    real_file_name = f.name
    save_file_name = str(image_id) + get_extension_name(real_file_name)

    #获取大图和小图的文件绝对路径
    parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    upload_path = os.path.join(parent_path, 'static/upload/')
    big_file_path = upload_path + 'big/' + save_file_name
    small_file_path = upload_path + 'small/' + save_file_name

    #保存大图
    destination = open(big_file_path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

    #保存缩略图
    create_thumbnails(big_file_path, small_file_path, 2)

    #写入数据表user_image中
    UserImage.objects.create(pic_real_name=real_file_name,
                             pic_save_name=save_file_name,
                             user_id=user_id, status=0,
                             title=request.POST['title'],
                             create_time=datetime.datetime.now())


def get_moods(request):
    """
    获取所有人发表的心情
    """
    return render_to_response("main/moods.html",
                                  {'menu_active': 'moods'},
                                  context_instance=RequestContext(request))