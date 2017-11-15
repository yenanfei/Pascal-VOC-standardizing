from pascal_voc_io import PascalVocWriter
from pascal_voc_io import PascalVocReader
import os
import cv2
import sys

#generate label
#folder for generated images
foldername = 'JPEGImages'
#format: 000001.jpg

filename = ''
imgSize = [0,0,0]
localImagePath = ''
xmlfname = ''


for line in open('boxes.txt'):
    dot = line.find('.')
    underline = dot - 6
    start = dot - 6
    end = dot + 4
    filename = line[underline:end]
    purename = line[start:dot]
    print filename
    print purename
    localImagePath = '/home/guhuxiang/darknet/scripts/VOCdevkit/VOCtest/JPEGImages/'+filename
    xmlfname = '/home/guhuxiang/darknet/scripts/VOCdevkit/VOCtest/Annotations/'+purename+'.xml'
    break

readimagename = '/home/guhuxiang/darknet/scripts/VOCdevkit/VOCtest/JPEGImages/{}'.format(filename)
print readimagename
img = cv2.imread(readimagename,0)
#img = cv2.cv.LoadImage(readimagename,CV_LOAD_IMAGE_COLOR)
print img.shape
imagesize = [img.shape[0],img.shape[1],1]

#print xmlfname
writer = PascalVocWriter(foldername,filename,imgSize,localImgPath=localImagePath)

count = 0
for line in open('boxes.txt'):
    if count == 0:
        count += 1
        pass
    else:

        print line
        coors = line.split(' ')
   
        xmin = int(coors[0])
        ymin = int(coors[1])
        xmax = int(coors[2])
        ymax = int(coors[3])
        num = int(coors[4])
    
        writer.addBndBox(xmin,ymin,xmax,ymax,num,0)
        
writer.verified = False
writer.save(xmlfname)
