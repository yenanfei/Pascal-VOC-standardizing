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
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(file))
    return L
file_dir='/root/darknet/scripts/VOCdevkit/VOCaccuracy/wat1212/'
goal_dir='/root/darknet/scripts/VOCdevkit/VOCaccuracy/wat1212black/'
for name in file_name(file_dir):
    img = cv2.imread(file_dir+name);
    dot = name.find('.')
    # namenum=int(name[:dot])
    rows, cols, channels = img.shape
    for i in range(rows):
        for j in range(cols):
            for c in range(3):
            	img[i,j][c]=255-img[i,j][c]
                    
    cv2.imwrite(goal_dir+name, img)