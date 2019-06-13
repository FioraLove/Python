# coding=gbk
import socket

server = socket.socket()
server.bind(('localhost', 6969))  # 绑定要监听的接口
server.listen()  # 监听

print('我要开始等电话了')
conn, addr = server.accept()  # 等待响应
# conn就是客户端连过来而在服务端为其生成的一个连接实例
print(conn, addr)

print('电话来了')
data = conn.recv(1024)
print('recv:', data)
conn.send(data.upper())

server.close()
