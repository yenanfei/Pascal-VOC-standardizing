# -*- coding: <utf-8> -*-
import xml.dom.minidom
import Queue
import sys
import random
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
        # print file_dir
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(file))
                #print L
    return L

file_dir='/root/caffe-ssd/data/VOCdevkit/mydataset/Annotations/'
goal_dir='/root/caffe-ssd/data/VOCdevkit/mydataset/Annotations/'
for name in file_name(file_dir+'/'):
    # print(name)
    xmaxque = Queue.Queue()
    # print file_dir+dirs+name
    dom1=xml.dom.minidom.parse(file_dir+name)
    root=dom1.documentElement
    #print root.nodeName,',',root.nodeValue,',',root.nodeType
       
    node1=root.getElementsByTagName('name')
    for tmp1 in node1:
        for tmp1 in tmp1.childNodes:
            if (len(tmp1.data)>1):
            	print name
            tmp1.data=int(tmp1.data)
            if (tmp1.data<0 or tmp1.data>9):
            	print name

    #f = open(goal_dir+name+'.xml', 'w')
    #dom1.writexml(f)
    #f.close()
