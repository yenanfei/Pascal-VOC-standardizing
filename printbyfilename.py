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

file_dir='/home/guhuxiang/darknet/scripts/VOCdevkit/VOC2030/Annotations/'
f = open('train.txt','w')
for name in file_name(file_dir):
        dot=name.find('.')
        f.write(name[:dot]+'\n')
f.close()
