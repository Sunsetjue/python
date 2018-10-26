'''
TCP编程

面向链接的传输，即每次传输之前需要先建立一个链接
客户端和服务器端两个程序需要编写
Server端的编写流程
建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后从新建立的socket
绑定端口和地址
监听接入的访问socket
接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
接受对方的发送内容，利用接收到的socket接收内容
如果有必要，给对方发送反馈信息
关闭链接通路
Client端流程
建立通信socket
链接对方，请求跟对方建立通路
发送内容到对方服务器
接受对方的反馈
关闭链接通路
'''

#编写服务端
import socket
def server():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr = ('127.0.0.1',10074)
    sock.bind(addr)
    sock.listen(1)
    #监听接入访问的socket
    while True:
        # 4. 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
        # accept返回的元祖第一个元素赋值给skt，第二个赋值给addr
        skt,addr = sock.accept()
        msg = skt.recv(300)#这里是recv()
        print(msg.decode())
        word = 'I love SongYue'
        skt.send(word.encode())#发送过去这里则是用的send
        skt.close()
if __name__ == '__main__':
    print('Server start .....')
    server()
    print('Server down ....')

