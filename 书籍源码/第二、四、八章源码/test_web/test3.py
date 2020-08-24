#import socket
from  wsgiref.simple_server import make_server

def index(url):
    with open('index.html', 'r',encoding='utf-8') as f:
        rd = f.read()
        rd=rd.replace("$@index$@", "首页")
    return bytes(rd,encoding='utf-8')

def test(url):
    with open('test.html', 'r',encoding='utf-8') as f:
        rd = f.read()
        rd = rd.replace("$@test$@", "测试")
    return bytes(rd,encoding='utf-8')

def fun404(url):
    ret = "<h1>not found!</h1>"
    return bytes(ret, encoding='utf-8')


url_func=[
    ("/index/",index),
    ("/test/",test),

]

def run_server(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html;charset=utf-8'),])#设置http响应的状态码和头信息
    url=environ['PATH_INFO']
    func = None
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    if func:
        resp = func(url)
    else:
        resp = fun404(url)
    return [resp,]

if __name__=='__main__':
    httpd=make_server('127.0.0.1',8000,run_server)
    print('正在监听…………')

    httpd.serve_forever()
