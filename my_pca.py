import numpy as np
import cv2
import os

def estimate_dim(vals, percent, default = 0):
    if default != 0:
        return default
    sortArray=np.sort(vals)[::-1] # 特征值从大到小排序
    pct = np.sum(sortArray)*percent
    tmp = 0
    num = 0
    for eigVal in sortArray:
        tmp += eigVal
        num += 1
        if tmp>=pct:
            return num

def pca(data, percent, default_dim = 0):
    # 得到去中心化数据，非必要
    meanVals = np.mean(data, axis=0)
    meanRemoved = data - meanVals

    # 计算协方差矩阵
    covMat = np.dot(np.transpose(meanRemoved), meanRemoved)/(data.shape[0]-1)

    # 协方差的特征值、特征向量
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))

    # 设定主成分个数
    k = estimate_dim(eigVals, percent, default_dim)
    #print('K =', k)

    #对特征值eigVals从大到小排序
    eigValInd = np.argsort(eigVals)[::-1]
    eigValInd = eigValInd[:k]
    # 主成分
    redEigVects = eigVects[:,eigValInd]
    # 将原始数据投影到主成分上得到新的低维数据lowDDataMat
    lowDDataMat = meanRemoved*redEigVects
    # 得到重构数据reconMat
    reconMat = (lowDDataMat*redEigVects.T)+meanVals
    
    return lowDDataMat, reconMat

if __name__ == '__main__':
    imagesDir = "/standset"
    rootdir = os.getcwd()  #获取当前目lu
    list = os.listdir(rootdir + imagesDir) #列出文件夹下所有的目录与文件
    writeDir = "/compressed/pca_k16"

    for index in range(0, len(list)):
        path = os.path.join(rootdir + imagesDir, list[index])
        pic = cv2.imread(path)
        #cv2.imshow('origin', pic)
        #cv2.imwrite('compressed/001.jpg', pic, [int( cv2.IMWRITE_JPEG_QUALITY), 75])
        for i in range(3):
            temp = pic[:,:,i]
            data = np.mat(temp)
            low_data, recon_data = pca(data, 1, 16)
            #print('原始数据', temp.shape, '降维数据', low_data.shape)
            #print(data)
            #print(recon_data)
            recon_data = np.array(recon_data, dtype='uint8')
            pic[:,:,i] = recon_data

        cv2.imwrite(os.path.join(rootdir + writeDir, list[index]), pic, [int( cv2.IMWRITE_JPEG_QUALITY), 75])
        print("wirting ", index , "into " + imagesDir + list[index])
        #cv2.imshow('temp', pic)
        #cv2.imshow('recon_data', recon_data)
        #cv2.waitKey(10000)
        #print_error(np.array(temp, dtype='double'), np.array(recon_data,
        #        dtype='double'))
    print("all done!")
