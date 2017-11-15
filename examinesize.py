# -*- coding: <utf-8> -*-
import xml.dom.minidom
import Queue
import cv2
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

file_dir='C:\\Users\\WhyTensorFlow\\Desktop\\xml\\'
for name in file_name(file_dir):
        # print(name)
        xmaxque = Queue.Queue()
        # print file_dir+dirs+name
        dom1=xml.dom.minidom.parse(file_dir+name)
        root=dom1.documentElement
        #print root.nodeName,',',root.nodeValue,',',root.nodeType

        picpath= root.getElementsByTagName('path')[0]
        for picpath in picpath.childNodes:
        	print picpath.data
        im = cv2.imread(picpath.data)

        nodewidth= root.getElementsByTagName('width')[0]
        for nodewidth in nodewidth.childNodes:
            #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
            nodewidth.data=im.shape[1]
            tmpwidth=int(nodewidth.data)
            #print tmpwidth

        nodeheight= root.getElementsByTagName('height')[0]
        for nodeheight in nodeheight.childNodes:
            #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
            tmpheight=int(nodeheight.data)
            nodeheight.data=im.shape[0]
            #print tmpheight

        depth= root.getElementsByTagName('depth')[0]
        for depth in depth.childNodes:
            #if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
            tmpdepth=int(depth.data)
            depth.data=im.shape[2]
            #print tmpdepth

        f = open(file_dir+name, 'w')
        dom1.writexml(f)
        f.close()
