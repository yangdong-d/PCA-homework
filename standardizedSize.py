import os
import PIL.Image

imagesDir = "/image_set"
rootdir = os.getcwd()  #获取当前目录
list = os.listdir(rootdir + imagesDir) #列出文件夹下所有的目录与文件

outDir = rootdir + "/standset/"
len_x = 0
len_y = 0
pic_nums = 0
for i in range(0,len(list)):
    path = os.path.join(rootdir + imagesDir, list[i])
    #print(path)
    pic = PIL.Image.open(path)
    out = pic.resize((512, 512))
    out.save(outDir + list[i])
    print(i)
