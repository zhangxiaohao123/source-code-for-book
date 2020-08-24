from django.utils.deprecation import MiddlewareMixin

class middle1(MiddlewareMixin):
    def process_request(self,request):

        print('中间件1的processs_request运行,请求URL是：',request.path_info)
    def process_response(self,request,response):
        print('中间件1的process_response进行响应,状态短语：',response.reason_phrase)
        return response

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('中间件1的process_view运行')
    def process_exception(self,request,exception):
        print('中间件1的process_exception运行')

    def process_template_response(self, request, response):
        print("中间件1的process_template_response运行")
        return response

class middle2(MiddlewareMixin):
    def process_request(self, request):
        print('中间件2的processs_request运行，请求主机IP:{}端口号：{}'.format(request.META.get('REMOTE_ADDR'),request.META.get('SERVER_PORT')))

    def process_response(self, request, response):
        print('中间件2的process_response进行响应,状态码：',response.status_code)
        return response
    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('中间件2的process_view运行')
    def process_exception(self,request,exception):
        print('中间件2的process_exception运行')
    def process_template_response(self, request, response):
        print("中间件2的process_template_response运行")
        return response





