#-*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from util.tools import get_md5

__author__ = 'weichao02'


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password', 'email_address', 'status')
    fields = list_display
    search_fields = ('user_name',)
    actions = ('delete_selected',)

    def save_model(self, request, obj, form, change):
        """
        保存对象时, 需保存密码的md5值
        """
        obj.password = get_md5(obj.password)
        obj.save()


class LoginFreeAdmin(admin.ModelAdmin):
    list_display = ('path_prefix',)
    fields = list_display
    actions = ('delete_selected',)


class UserImageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'pic_real_name', 'pic_save_name', 'title', 'create_time')
    fields = list_display
    actions = ('delete_selected',)

admin.site.register(User, UserAdmin)
admin.site.register(LoginFree, LoginFreeAdmin)
admin.site.register(UserImage, UserImageAdmin)