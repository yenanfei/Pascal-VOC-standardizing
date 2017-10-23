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
        # print file_dir
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(file))
                # print L
    return L

def dir_name(file_dir):
    M = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        for name in dirs:
            M.append(os.path.join(name))
    return M

file_dir='D:\\new\\'

for dirs in dir_name(file_dir):
    # print dirs
    dirs=dirs+'\\'
    for name in file_name(file_dir+dirs+'\\'):
            # print(name)
            
            xmaxque = Queue.Queue()
            # print file_dir+dirs+name
            dom1=xml.dom.minidom.parse(file_dir+dirs+name)
            root=dom1.documentElement
            #print root.nodeName,',',root.nodeValue,',',root.nodeType
            node1=root.getElementsByTagName('name')
            for tmp in node1:
                for tmp in tmp.childNodes:
                    tmpname = tmp.data
                    #print tmpname
                    if tmpname=='A' or tmpname=='B' or tmpname=='C' or tmpname=='D' or tmpname=='9' or tmpname=='?':
                        delnode=tmp.parentNode.parentNode
                        root.removeChild(delnode)
                        #print node1.parentNode
                        #node1.removeAttribute('object')
                    #xmaxque.put(int(tmpxmin+0.03*tmpwidth))

            f = open(file_dir+dirs+name, 'w')
            dom1.writexml(f)
            f.close()