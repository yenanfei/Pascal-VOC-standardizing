from pascal_voc_io import PascalVocWriter
from pascal_voc_io import PascalVocReader
import os
import cv2

path = '/root/darknet/scripts/VOCdevkit/VOC2050back/Annotations/'
imgpath = '/root/darknet/scripts/VOCdevkit/VOC2050back/JPEGImages/'
pathdir = os.listdir(path)
for file in pathdir:
    filename = path + file
    print file
    dot = file.find('.')
    purename = file[:dot]
    reader = PascalVocReader(filename)
    reader.parseXML()
    boxes = []
    for i,shape in enumerate(reader.shapes):
        if i < (len(reader.shapes)/2):
            boxes.append(shape)
    boxes = sorted(boxes, key=lambda item:item[1][0][0])
    readimgname = 'VOCdevkit/VOC2050/JPEGImages/{}.jpg'.format(purename)
    img = cv2.imread(readimgname)
    imgSize = [img.shape[0],img.shape[1],1]
    foldername = 'JPEGImages'
    filename = purename+'.jpg'
    localImagePath = '/root/darknet/scripts/VOCdevkit/VOC2050back/JPEGImages/'+filename
    writer = PascalVocWriter(foldername,filename,imgSize,localImgPath=localImagePath)
    #print type(boxes)
    for b in boxes:
        writer.addBndBox(b[1][0][0],b[1][0][1],b[1][2][0],b[1][2][1],b[0],0)
        #print b
    writer.verified = False
    xmlfname = '/root/darknet/scripts/VOCdevkit/VOC2050back/Annotations/{}'.format(file)
    writer.save(xmlfname)
