# Pascal-VOC-standardizing
## changedata.py
changedata的代码用于批量修改xml文件中的一些数据，如果要使用，修改file_dir为自己的目录并且将之后修改数据的逻辑换成在自己的即可，我这里做的是读取全图的宽度并且取一个比例以后加上xmin，取代原来的xmax，是项目需求所要求的。
## standard.py
standard的代码用来将file_dir子目录下的所有xml中的路径替换成darknet中要求的路径格式（这个路径还要根据自己darknet的安装目录调整，修改change_dir即可），同时后缀统一成了jpg，要注意如果图片文件里有大写的JPG那么要修改为小写，否则不认，推荐使用ReNamer进行批量的重命名序列化等操作。
### 注意
这里默认了file_dir下至少还有一层目录，然后才放着xml文件。
## imagestandardizing.py
最近遇到了传输遇到图片损坏或者编码不规范的情况，低版本opencv不能读（由于我没有服务器的root权限因此），我查到的比较好的处理方法是用高版本opencv读入这些有问题的图片（可能会有warning，不用管他），再重新写一遍，这样图片就规范了。
## deletedata.py
这是用来删除一些类别的标注的，需要减少类别的时候可以使用。
## widerdata.py
由于yolo对于小物体的处理很不好，因此我这边尝试将它的标注的bounding box放大试一试。