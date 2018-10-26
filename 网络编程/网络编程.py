'''
TCP/UDP协议
UDP：非安全的不面向链接的传输

安全性差
大小限制64kb
没有顺序
速度快
TCP

基于链接的通信
SOCKET编程

socket（套接字）: 是一个网络通信的端点， 能实现不同主机的进程通信，网络大多基于Socket通信
通过IP+端口定位对方并发送消息的通信机制
分为UDP和TCP
客户端Client： 发起访问的一方
服务器端Server：接受访问的一方
UDP 编程

Server端流程 1. 建立socket，socket是负责具体通信的一个实例 2. 绑定，为创建的socket指派固定的端口和ip地址 3. 接受对方发送内容 4. 给对方发送反馈，此步骤为非必须步骤
Client端流程 1. 建立通信的socket 2. 发送内容到指定服务器 3. 接受服务器给定的反馈内容
'''

#编写服务端
import socket
def server():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #socket.AF_INET表示使用ipv4协议族
    #socket.SOCK_DGRAM表示使用UDP传输

    #绑定 IP地址和端口
    # 127.0.0.1: 这个ip地址代表的是机器本身
    # 地址是一个tuple类型，(ip, port)
    addr = ('127.0.0.1',10073)
    sock.bind(addr)

    # 接受对方消息
    # 等待方式为死等， 没有其他可能性
    # recvfrom接受的返回值是一个tuple，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    # rst = sock.recvfrom(500)
    msg_1, addr1 = sock.recvfrom(200)
    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf8
    text = msg_1.decode()
    print(text)
    #回消息
    world = 'hello,world'
    msg_2 = world.encode()
    sock.sendto(msg_2,addr1)
if __name__ == '__main__':
    print('Server start ......')
    server()
    print('Server down .......')
