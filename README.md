# Pascal-VOC-standardizing
## addflare.py
对图像全局选取一些随机的矩形框做random erasing。
## addflarebyxml.py
对标注框内的图像随机做random erasing。
## changedata.py
changedata的代码用于批量修改xml文件中的一些数据，如果要使用，修改file_dir为自己的目录并且将之后修改数据的逻辑换成在自己的即可，我这里做的是读取全图的宽度并且取一个比例以后加上xmin，取代原来的xmax，是项目需求所要求的。
## changetogray.py
将三通道的图转成灰度图像。
## deletebyfilename.py
如果文件名是纯数字，那么可以根据文件名大小来删除一定范围内的图片。
## deletedata.py
对于标注中的一类物体做整体删除。
## examinesize.py
有时候xml中的宽和高损失了，导致训练无法正常进行，这里利用python的cv2这个包进行修正
## imagestandardizing.py
最近遇到了传输遇到图片损坏或者编码不规范的情况，低版本opencv不能读（由于我没有服务器的root权限因此），我查到的比较好的处理方法是用高版本opencv读入这些有问题的图片（可能会有warning，不用管他），再重新写一遍，这样图片就规范了。
## k_means_yolo.py
yolo-voc.cfg中的anchors参数为预设的ImageNet中的anchors聚类结果。（yolo对fast-rcnn优化之一就是使用聚类的anchors替换了原来手工挑选的anchors，使得mAP提高了1%~2%），然而，对于自己的训练集，就需要重新聚类了。修改该文件的路径即可。
## pascal_voc_io.py
可以读写标准格式xml本目录下有些py文件可能需要引用这个文件。
## printbyfilename.py
有时候需要生成训练集\测试集列表，直接取文件名打印成txt
## standard.py
standard的代码用来将file_dir子目录下的所有xml中的路径替换成darknet中要求的路径格式（这个路径还要根据自己darknet的安装目录调整，修改change_dir即可），同时后缀统一成了jpg，要注意如果图片文件里有大写的JPG那么要修改为小写，否则不认，推荐使用ReNamer进行批量的重命名序列化等操作。
### 注意
这里默认了file_dir下至少还有一层目录，然后才放着xml文件。
## widerdata.py
由于yolo对于小物体的处理很不好，因此我这边尝试将它的标注的bounding box放大试一试。