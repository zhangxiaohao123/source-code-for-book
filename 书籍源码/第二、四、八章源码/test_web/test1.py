import socket

sk=socket.socket() # 建立socket服务
sk.bind(('127.0.0.1',8000))#绑定ip与端口，这是绑定本机端口
sk.listen()#进行监听
print('socket服务开始运行.....')
while True:
    conn,addr=sk.accept() #接收socket客户端联结
    data=conn.recv(1024) #接收socket客户端数据
    print(data)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")#向客户端发消息,字符串前加字母b表示以字节形式传输
    conn.send(bytes("我是socket服务端，我已接到你请求。",encoding='utf-8'))#向客户端发消息，bytes()函数把汉字字符串转换成字节形式

    conn.close()#关闭联结
    #sk.close()
