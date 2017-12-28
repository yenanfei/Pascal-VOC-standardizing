import cv2
import random
import os
from pascal_voc_io import PascalVocWriter
from pascal_voc_io import PascalVocReader


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
file_dir='/root/darknet/scripts/VOCdevkit/VOC2050_corrected/JPEGImages/'
goal_dir='/root/darknet/scripts/VOCdevkit/VOC2050_corrected/JPEGImages/'
xml_dir = '/root/darknet/scripts/VOCdevkit/VOC2050_corrected/Annotations/'
foldername = 'JPEGImages'
for name in file_name(file_dir):
    img = cv2.imread(file_dir+name);
    dot = name.find('.')
    namenum=int(name[:dot])
    newname=str(namenum+200000)
    xmlfname = xml_dir+name[:dot]+'.xml'
    print xmlfname
    reader = PascalVocReader(xmlfname)
    reader.parseXML()
    
    boxes = []
    for i,shape in enumerate(reader.shapes):
        if i < (len(reader.shapes)/2):
            boxes.append(shape)

    #print boxes
    for box in boxes:
        #print '--------'
        #print box
        section = random.randint(1,4)
        xmin = box[1][0][0]
        ymin = box[1][0][1]
        xmax = box[1][2][0]
        ymax = box[1][2][1]
        midx = (xmin+xmax)/2
        midy = (ymin+ymax)/2 
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0

        #print 'xmin:'+str(xmin)+' ymin:'+str(ymin)+' xmax:'+str(xmax)+' ymax'+str(ymax)+' midx:'+str(midx)+' midy:'+str(midy)
        if section==1:
            x0 = xmin
            y0 = ymin
            x1 = midx
            y1 = midy
        elif section==2:     
            x0 = midx
            y0 = ymin
            x1 = xmax
            y1 = midy  
        elif section==3:
            x0 = midx
            y0 = midy
            x1 = xmax
            y1 = ymax
        elif section==4:
            x0 = xmin
            y0 = midy
            x1 = midx
            y1 = ymax 
        #print 'section'+str(section)
        #print 'x0='+str(x0)+'x1='+str(x1)
        tmpimg=img[y0:y1, x0:x1]
        #print tmpimg.shape
        rows, cols, channels = tmpimg.shape
        dst = tmpimg.copy()
        a = random.uniform(0, 2)
        b = random.uniform(-100, 100)
        for i in range(rows):
            for j in range(cols):
                #print '======================'
                for c in range(3):
                    if tmpimg[i, j][c] * a + b > 255:
                        dst[i, j][c] = tmpimg[i, j][c]
                        #print 'a'
                    elif tmpimg[i, j][c] * a + b < 0:
                        dst[i, j][c] = tmpimg[i, j][c]
                        #print 'b'
                    else :
                        dst[i, j][c] = tmpimg[i, j][c] * a + b
                        #print 'c'
                        #print a
                    #print str(dst[i, j][c])+"/"+str(tmpimg[i, j][c])
                    

        img[y0:y1, x0:x1]=dst
    imgSize = [img.shape[0],img.shape[1],1]   
    localImagePath = '/root/darknet/scripts/VOCdevkit/VOC2050_corrected/JPEGImages/'+newname+'.jpg'
    newxmlfname = '/root/darknet/scripts/VOCdevkit/VOC2050_corrected/Annotations/'+newname+'.xml'
    writer = PascalVocWriter(foldername,newname+'.jpg',imgSize,localImgPath=localImagePath)
    writer.verified = False
    for i,shape in enumerate(reader.shapes):
        if i<(len(reader.shapes)/2):
            writer.addBndBox(shape[1][0][0],shape[1][0][1],shape[1][2][0],shape[1][2][1],shape[0],0)
    writer.save(newxmlfname)
    cv2.imwrite(goal_dir+newname+'.jpg', img)
    print goal_dir+newname
