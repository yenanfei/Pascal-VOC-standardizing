import cv2
import random
import os

def file_name(file_dir):
    # print file_dir
    L = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        #print file_dir
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(file))
    return L
file_dir='/home/guhuxiang/darknet/scripts/VOCdevkit/VOC2030/JPEGImages/'
goal_dir='/home/guhuxiang/darknet/scripts/VOCdevkit/VOC2040/JPEGImages/'
for name in file_name(file_dir):
    img = cv2.imread(file_dir+name);
    for i in range(1,10):
        x0=random.randint(0,img.shape[0]-2)
        x1=random.randint(x0+2,img.shape[0])
        y0=random.randint(0,img.shape[1]-2)
        y1=random.randint(y0+2,img.shape[1])
        tmpimg=img[x0:x1, y0:y1]
        rows, cols, channels = tmpimg.shape
        dst = tmpimg.copy()
        a = random.uniform(0.5, 1.5)
        b = random.uniform(-50, 50)
        for i in range(rows):
            for j in range(cols):
                for c in range(3):
                    if tmpimg[i, j][c] * a + b > 255:
                        dst[i, j][c] = tmpimg[i, j][c]
                    elif tmpimg[i, j][c] * a + b < 0:
                        dst[i, j][c] = tmpimg[i, j][c]
                    else :
                        dst[i, j][c] = tmpimg[i, j][c] * a + b

        img[x0:x1, y0:y1]=dst
    cv2.imwrite(goal_dir+name, img);
    print goal_dir+name