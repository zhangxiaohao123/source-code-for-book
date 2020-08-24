from django.conf import settings
from django.shortcuts import HttpResponse, redirect
from django.utils.deprecation import MiddlewareMixin
import re
from django.urls import converters
#
# class MiddlewareMixin(object):
#     def __init__(self, get_response=None):
#         self.get_response = get_response
#         super(MiddlewareMixin, self).__init__()
#
#     def __call__(self, request):
#         response = None
#         if hasattr(self, 'process_request'):
#             response = self.process_request(request)
#         if not response:
#             response = self.get_response(request)
#         if hasattr(self, 'process_response'):
#             response = self.process_response(request, response)
#         return response


class RbacMiddleware(MiddlewareMixin):
    """
    检查用户的url请求是否是其权限范围内
    """
    def process_request(self, request):
        request_url = request.path_info
        permission_url = request.session.get(settings.PERMISSION_URL_KEY)
        print('访问url', request_url)
        print('权限--', permission_url)

        # 如果请求url在白名单，放行
        for url in settings.SAFE_URL:
            if re.match(url, request_url):
                return None


        # 2、超级用户免所有权限

        if request.user.is_superuser:
            #print('aaaaaaaaaaa')
            return None
        # 如果未取到permission_url, 定向至登录；
        if not permission_url:
            return redirect(settings.LOGIN_URL)
        # #针对django 2.0 path中URL表达式，修改成常规正则表达式
        #
        # for perm_group_id,code_url in permission_url.items():
        #     urls1 = []
        #     for url in code_url['urls']:
        #         url = re.sub('<int:\w+>', '[0-9]+',url)
        #         url = re.sub('<str:\w+>', '[^/]+', url)
        #         url = re.sub('<slug:\w+>','[-a-zA-Z0-9_]+', url)
        #         url = re.sub('<uuid:\w+>', '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', url)
        #         urls1.append(url)
        #     del code_url['urls']
        #     code_url['urls']=urls1




        # 循环permission_url，作为正则，匹配用户request_url
        # 正则应该进行一些限定，以处理：/user/ -- /user/add/匹配成功的情况
        flag = False

        for perm_group_id,code_url in permission_url.items():

            for url in code_url['urls']:

                url_pattern = "^{0}$".format(url)
                print(url_pattern)
                if re.match(url_pattern, request_url):
                    request.session['permission_codes']=code_url["codes"]
                    flag = True
                    break
            if flag:
                return None
        if not flag:
            #如果是调试模式，显示可访问url
            if settings.DEBUG:
                info = '<br/>' + ('<br/>'.join(code_url['urls']))
                return HttpResponse('无权限，请尝试访问以下地址：%s' % info)
            else:
                return HttpResponse('无权限访问')


