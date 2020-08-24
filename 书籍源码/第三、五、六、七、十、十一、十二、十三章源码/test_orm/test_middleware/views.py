from django.shortcuts import render,HttpResponse

# Create your views here.
def test(request):
    print('test视图函数运行')
    return HttpResponse('hello world!')

class test_temp(object):
    def __init__(self,response):
        self.response=response
    def render(self):
        return self.response

def test2(request):
    print('test2函数运行,主要为了测试processing_template_response中间件是否运行！！')
    resp=HttpResponse('hello world,this is  test2')
    return test_temp(resp)

