from django.http import HttpResponseRedirect

__author__ = 'weichao02'
from ..util.tools import get_param_string, is_need_to_login, is_logined_in
from ..settings import LOGIN_TIMEOUT


class MainMiddleWare(object):

    def process_request(self, request):
        path = request.path
        param_string = get_param_string(request)
        if param_string:
            full_path = path + '?' + param_string
        else:
            full_path = path
        referer = request.META.get('HTTP_REFERER', '')
        if -1 != referer.find('/user/reg-user/'):
            return None
        print referer
        if path == '/user/login/' or not is_need_to_login(full_path):
            return None
        user = is_logined_in(request)
        if user:
            return None
        response = HttpResponseRedirect("/user/login")
        response.set_cookie("next-url", full_path, LOGIN_TIMEOUT)
        return response
