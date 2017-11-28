import os

count = 1
path = 'JPEGImages'

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        newname = '{:06d}.jpg'.format(count)
        count += 1
        os.rename(os.path.join(path,file),os.path.join(path,newname))
        print newname
