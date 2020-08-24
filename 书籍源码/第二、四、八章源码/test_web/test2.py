import socket

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

sk=socket.socket() # 建立socket服务
sk.bind(('127.0.0.1',8000))#绑定ip与端口，这是绑定本机端口
sk.listen()#进行监听
print('socket服务开始运行.....')

while True:
    conn, addr = sk.accept()  # 接收socket客户端联结
    data = conn.recv(1024)  # 接收socket客户端数据
    print(data)
    if not data:
        continue #如果客户端没有发新的数据，就重新开始，不再向下执行。

    data_str = str(data, encoding='utf-8')#把收到的数据由字节转成字符串
    line= data_str.split("\r\n")
    print(line[0])
    v1= line[0].split()# 按照空格切割上面的字符串
    url =v1[1]
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")  # 向客户端发消息,字符串前加字母b表示以字节形式传输
    func=None
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    if func:
        func=func
    else:
        func = fun404

    rep = func(url)
    conn.send(rep)
    conn.close()

