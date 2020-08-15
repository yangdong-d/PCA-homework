# 概述

本文主要介绍使用PCA算法对图像进行压缩处理。
包括：统一图像尺寸、PCA算法、信息损失评估、压缩后存储空间统计。
[实践报告](https://test-34.su.bcebos.com/report.pdf)

### 环境

- Python3.76
- MACOS

### 快速开始

- 统一图像尺寸

把原图像缩放为512*512

```shell
python3 standardizedSize.py
```
- pca压缩

```shell
python3 my_pca.py
```

- 统计压缩效果

```
python3 print_error.py
```

### 目录结构
```text
51194507017-杨东东-实践报告（图像压缩）
├── 51194507017-杨东东-实践报告（图像压缩).docx    // 实践报告
├── compressed                                     // 压缩图像
├── imageset                                       // 原始图像
├── my_pca.py                                      // pca压缩
├── print_error.py                                 // 效果评估
├── README.md
├── standardizedSize.py                            // 图像尺寸统一
├── standset                                       // 512*512图像
```

### 实验效果

![avatar](https://test-34.su.bcebos.com/pca.jpg)
