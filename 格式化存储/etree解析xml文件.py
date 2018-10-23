import xml.etree.ElementTree
doc = xml.etree.ElementTree.parse('bedroom.xml')
root1 = doc.getroot()#得到根元素
print(root1)
root = doc.getiterator()#得到可迭代的集合
for i in root:
    print('{} - - - {}'.format(i.tag,i.text))
print('\n')
people = root1.find('Sunbin')#指定子元素,定向来查找
for j in people:
    print('{}----{}'.format(j.tag,j.text))