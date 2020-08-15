import numpy as np
import os
import cv2
from PIL import Image
import io

def print_error(rootDir, imagesDir, recDir, ori_list):
    error_min = 10000.0
    error_max = -0.01
    error_avg = 0.0

    for index in range(0, len(ori_list)):
        path1 = os.path.join(rootDir + imagesDir, ori_list[index])
        pic1 = cv2.imread(path1)
        path2 = os.path.join(rootDir + recDir, ori_list[index])
        pic2 = cv2.imread(path2)

        for i in range(3):
            sum1 = 0
            sum2 = 0
            data = pic1[:,:,i].astype(np.int32)
            rec_data = pic2[:,:,i].astype(np.int32)
            diff = data - rec_data
            for j in range(data.shape[0]):
                sum1 += np.dot(data[j], data[j])
                sum2 += np.dot(diff[j], diff[j])
            print('丢失信息量：', sum2)
            print('原始信息量：', sum1)
            print('信息丢失率：', sum2/sum1)
            error = sum2/sum1
            error_min = error if error < error_min else error_min
            error_max = error if error > error_max else error_max
            error_avg = ((index * 3 + i) * error_avg + error) / (index * 3 + i + 1)
            print(error, error_min, error_max, error_avg)
        print("do ", index)
    print("all done!")
    print(error_min, error_max, error_avg)  

def print_compress(rootDir, imagesDir, recDir, ori_list):
    cmin = 1000.0
    cmax = -0.01
    cavg = 0

    for index in range(0, len(ori_list)):
        path1 = os.path.join(rootDir + imagesDir, ori_list[index])
        path2 = os.path.join(rootDir + recDir, ori_list[index])
        if index == 91:
            continue
        img1 = Image.open(path1)
        img2 = Image.open(path2)
        imgByteArr1 = io.BytesIO()
        imgByteArr2 = io.BytesIO()
        img1.save(imgByteArr1, format='JPEG')
        img2.save(imgByteArr2, format='JPEG') 
        imgByteArr1 = imgByteArr1.getvalue()
        imgByteArr2 = imgByteArr2.getvalue()
        c = len(imgByteArr2) / len(imgByteArr1)

        cmin = c if c < cmin else cmin
        cmax = c if c > cmax else cmax
        cavg = (index * cavg + c) / (index + 1)

        print(c, cmin, cmax, cavg, index)
        if c > 2:
            print(ori_list[index])
    print("all done!")
    print(cmin, cmax, cavg)

if __name__ == '__main__':
    imagesDir = "/standset"
    recDir = "/compressed/pca_k128"
    rootdir = os.getcwd()  #获取当前目
    ori_list = os.listdir(rootdir + imagesDir) #列出文件夹下所有的目录与文件
    #print_error(rootdir, imagesDir, recDir, ori_list)
    print_compress(rootdir, imagesDir, recDir, ori_list)
