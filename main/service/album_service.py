#-*- coding: utf-8 -*-
__author__ = 'weichao02'
from ..models import UserImage


def get_mine_image_list(user_id, page_num):
    """
    分页获取我的图片列表
    """
    page_size = 10
    offset = 10 * page_num
    image_list = UserImage.objects.filter(user_id=user_id)
    if not image_list:
        return None
    return image_list[offset: page_size]
