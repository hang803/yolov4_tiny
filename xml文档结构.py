from xml.etree import ElementTree as ET
import os

in_file=os.path.join('VOCdevkit/VOC2007/Annotations','(1).xml')
tree=ET.parse(in_file)
print(type(tree))

root=tree.getroot()
print(type(root),'\n',root.tag)

for index,child in enumerate(root):
  print('the{},node:{},'.format(index,child.tag))
  for i,child_child in enumerate(child):
    print('    the{},name:{},text:{}'.format(i,child_child.tag,child_child.text))
print(root.find('object'))
