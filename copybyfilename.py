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

file_dir='D:\\datasetbakup\\VOC2050v2\\Annotations\\'
for name in file_name(file_dir):
        namenum=int(name[:6])
        print namenum
        namenum=namenum+100000
        newname=str(namenum)+'.xml'
        command = 'cp '+file_dir+name+' D:\\datasetbakup\\VOC2050v2\\Annotations\\'+newname
        print command
        os.system(command)
