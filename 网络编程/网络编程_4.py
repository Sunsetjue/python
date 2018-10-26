#编写TCP的客户端
import socket
def client():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    msg = 'hi'
    # 链接对方，请求跟对方建立通路
    addr = ('127.0.0.1',10074)
    sock.connect(addr)
    #发送消息
    sock.send(msg.encode())
    #接受对方的反馈
    data = sock.recv(300)
    print(data.decode())
    sock.close()
if __name__ == '__main__':
    client()
