#-*- coding: utf-8 -*-
from django.db import models

__author__ = 'weichao02'


class User(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    user_name = models.CharField(db_column="user_name", unique=True, max_length=255,
                                 verbose_name='用户名', blank=False, null=False)
    password = models.CharField(db_column="password", max_length=255,
                                verbose_name="密码", blank=False, null=False)
    email_address = models.EmailField(db_column="email_address", max_length=255, blank=True, verbose_name="邮箱")
    status = models.IntegerField(db_column="status", blank=True, null=True, verbose_name="状态", default=0)

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'


class LoginFree(models.Model):
    """
    免登陆的请求
    """
    id = models.AutoField(db_column="id", primary_key=True)
    path_prefix = models.CharField(max_length=255, db_column="path_prefix")

    class Meta:
        db_table = 'login_free'
        verbose_name = '免登录的url表'


class UserImage(models.Model):
    """
    用户上传的图片表
    """
    id = models.AutoField(db_column="id", primary_key=True)
    pic_real_name = models.CharField(db_column="pic_real_name", max_length=50)
    pic_save_name = models.CharField(db_column="pic_save_name", max_length=50)
    user_id = models.BigIntegerField(db_column="user_id")
    title = models.CharField(db_column="title", max_length=50)
    status = models.IntegerField(db_column="status", default=0, blank=True, null=True)
    create_time = models.DateTimeField(db_column="create_time", verbose_name="上传时间")

    class Meta:
        db_table = 'user_image'
        verbose_name = '用户上传图片表'