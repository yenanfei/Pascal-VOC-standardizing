# -*- coding: <utf-8> -*-

import cv2
import os

def file_name(file_dir):
    # print file_dir
    L = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        #print file_dir
        for file in files:
            L.append(os.path.join(file))
    return L

file_dir='G:\\orc\\meter1_2_fusion_val\\'
#file_dir='C:\\Users\\hasee\\Desktop\\xml\\'
goal_dir='G:\\newocr\\meter1_2_fusion_val\\'
for name in file_name(file_dir):
    print(name)
    im = cv2.imread(file_dir+name)
    cv2.imwrite(goal_dir+name,im)