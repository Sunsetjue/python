#编写客户端
import socket
def client():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    msg = '你好'
    data = msg.encode()
    sock.sendto(data,('127.0.0.1',10073))
    msg_1, addr = sock.recvfrom(200)
    message = msg_1.decode()
    print(message)
if __name__ == '__main__':
    client()