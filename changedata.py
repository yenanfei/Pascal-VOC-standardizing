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

file_dir='C:\\Users\\hasee\\Desktop\\third\\'
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
            node= root.getElementsByTagName('width')[0]
            for node in node.childNodes:
                #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
                tmpwidth=int(node.data)
                print node.data#get the width
            node1=root.getElementsByTagName('xmin')
            for tmp in node1:
                for tmp in tmp.childNodes:
                    tmpxmin = int(tmp.data)
                    print tmpxmin#get xmin
                    xmaxque.put(int(tmpxmin+0.03*tmpwidth))

            node2=root.getElementsByTagName('xmax')
            for tmp1 in node2:
                for tmp1 in tmp1.childNodes:
                    print 'orign:'+str(tmp1.data)
                    tmp1.data=xmaxque.get()
                    print 'new:'+str(tmp1.data)

            f = open(file_dir+dirs+name, 'w')
            dom1.writexml(f)
            f.close()
