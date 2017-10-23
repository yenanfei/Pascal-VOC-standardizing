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

file_dir='D:\\test\\'
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

            nodewidth= root.getElementsByTagName('width')[0]
            for nodewidth in nodewidth.childNodes:
                #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
                tmpwidth=int(nodewidth.data)

            nodeheight= root.getElementsByTagName('height')[0]
            for nodeheight in nodeheight.childNodes:
                #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
                tmpheight=int(nodeheight.data)

            node1=root.getElementsByTagName('xmin')
            for tmp1 in node1:
                for tmp1 in tmp1.childNodes:
                    tmpxmin = int(tmp1.data)
                    tmp1.data=int(tmpxmin-0.006*tmpwidth)

            node2=root.getElementsByTagName('xmax')
            for tmp2 in node2:
                for tmp2 in tmp2.childNodes:
                    tmpxmax = int(tmp2.data)
                    tmp2.data=int(tmpxmax+0.006*tmpwidth)

            node3=root.getElementsByTagName('ymin')
            for tmp3 in node3:
                for tmp3 in tmp3.childNodes:
                    tmpymin = int(tmp3.data)
                    tmp3.data=int(tmpymin-0.003*tmpheight)

            node4=root.getElementsByTagName('ymax')
            for tmp4 in node4:
                for tmp4 in tmp4.childNodes:
                    tmpymax = int(tmp4.data)
                    tmp4.data=int(tmpymax+0.003*tmpheight)

            f = open(file_dir+dirs+name, 'w')
            dom1.writexml(f)
            f.close()
