#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods

__author__ = 'weichao02'

@require_http_methods(['GET'])
def render_base(request):
    """
    测试直接跳转至base.html
    """
    return render_to_response('main/base.html')