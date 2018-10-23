import xml.dom.minidom
#在内存中创建一个空白文档
doc = xml.dom.minidom.Document()
#创建一个根节点Mangers
root = doc.createElement('Bedroom')
#设置跟节点属性
root.setAttribute('type','university')
root.setAttribute('location','营口理工学院')
#将根节点放到doc空白文档里面
doc.appendChild(root)

#创建一个需要写入xml的内容
msg = [{'name':'SunBin','age':21,'hobby':'sleep'},
       {'name':'JiangBaoLong','age':22,'hobby':'watching TV'},
       {'name':'PengKaiYi','age':23,'hobby':'play phones'},
       {'name':'LiuYang','age':23,'hobby':'play basketball'}]
for i in msg:
    #设置叶子节点，根节点的下属节点
    name = doc.createElement('name')
    name.appendChild(doc.createTextNode(i['name']))
    age = doc.createElement('age')
    age.appendChild(doc.createTextNode(str(i['age'])))
    hobby = doc.createElement('hobby')
    hobby.appendChild(doc.createTextNode(i['hobby']))
#将各子节点添加到跟节点中，如果有父类，先添加到父类，父类再添加到根节点
    root.appendChild(name)
    root.appendChild(age)
    root.appendChild(hobby)
#写入xml文档
xml = open(r'C:\Users\l\PycharmProjects\sunbin_1\室友基础信息.xml','w')
doc.writexml(xml,indent='\t',addindent='\t',newl='\n',encoding='utf-8')