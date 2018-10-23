import xml.dom.minidom
from xml.dom.minidom import parse
#使用minidom打开xml文件
p = xml.dom.minidom.parse('bedroom.xml')
#得到文件的根元素
doc = p.documentElement
for i in doc.childNodes:#获得一个可迭代的子元素.i.nodeName获得子元素
    if i.nodeName == 'Sunbin':
        print('Node"{}'.format(i.nodeName))
        feature = i.childNodes
        for j in feature:#获得元素的叶子元素,j.nodeName获得叶子元素
            if j.nodeName == 'age':
                print('age:{}'.format(j.childNodes[0].data))


