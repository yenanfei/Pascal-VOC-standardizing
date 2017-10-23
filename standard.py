# -*- coding: <utf-8> -*-
import xml.dom.minidom
import Queue
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#print sys.getdefaultencoding()

import os


def file_name(file_dir):
    # print file_dir
    L = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        #print file_dir
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(file))
    return L

file_dir='D:\\new\\'
#file_dir='C:\\Users\\hasee\\Desktop\\xml\\'
change_dir='/home/guhuxiang/darknet/scripts/VOCdevkit/VOC2023/JPEGImages/'
for name in file_name(file_dir):
        # print(name)
        xmaxque = Queue.Queue()
        # print file_dir+dirs+name
        dom1=xml.dom.minidom.parse(file_dir+name)
        root=dom1.documentElement
        #print root.nodeName,',',root.nodeValue,',',root.nodeType
        node= root.getElementsByTagName('filename')[0]
        for node in node.childNodes:
            #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
            node.data=name[:6]+'.jpg'
        node1= root.getElementsByTagName('path')[0]
        for node1 in node1.childNodes:
            #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
            node1.data=change_dir+name[:6]+'.jpg'

        f = open(file_dir+name, 'w')
        dom1.writexml(f)
        f.close()
