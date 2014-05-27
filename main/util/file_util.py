#-*- coding: utf-8 -*-
from PIL import Image

__author__ = 'weichao02'
import os


def get_extension_name(file_name):
    """
    获取文件后缀名
    """
    return os.path.splitext(file_name)[1]


def create_thumbnails(big_file_path, small_file_path, multiple):
    """
    创建缩略图
    """
    try:
        original = Image.open(big_file_path)
        (width, height) = original.size
        after_size = (width/multiple, height/multiple)
        original.thumbnail(after_size)
        original.save(small_file_path)
    except Exception as e:
        print e

if __name__ == '__main__':
    print(get_extension_name('a.wei.png.2'))
