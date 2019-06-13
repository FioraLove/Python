#  coding= gbk
import socket

client = socket.socket()  # 声明socket类，同时生成socket连接对象
client.connect(('localhost', 6969))
while True:
    msg = input('>>:').strip()
    client.send(msg.encode('utf-8'))  # 必须要写上‘b’，不然会出现TypeError: a bytes-like object is required, not 'str'
    data = client.recv(1024)
    print('recv:', data.decode())

client.close()
