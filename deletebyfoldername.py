# -*- coding: <utf-8> -*-
import xml.dom.minidom
import Queue
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#print sys.getdefaultencoding()

import os
import shutil
file_dir='D:\\cloud\\images\\images_320-240_2\\'
for root, dirs, files in os.walk(file_dir):
    # print(root)
    print(dirs)
    for dir in dirs:
        if dir=='Depth':
            shutil.rmtree(root+'\\'+dir)

        