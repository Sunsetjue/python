import asyncio

@asyncio.coroutine
def wget(host):
    print('wget {}....'.format(host))
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    #对于writer.drain()的用法,它会阻塞如果writer的buffer已经满了…当然在我们这个例子里面buffer是充足的,因为我们只发送了几个GET请求。
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s'%(host,line.decode('utf-8').rstrip()))
        #rstrip()函数表示返回删除 string 字符串末尾的指定字符后生成的新字符串。默认值为空格
    writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
asyncio
python3.4开始引入的标准库,内置了对移步io的支持
asyncio本身是一个消息循环,
步骤
创建消息循环
把协程导入
关闭
'''
