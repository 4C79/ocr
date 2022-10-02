import numpy as np
import torchvision.transforms as transforms
from PIL import Image
import os


def image_RGB2Gray(imgdir):
    # 图片路径，相对路径
    imgList = os.listdir(imgdir)
    for i in range(len(imgList)):
        img_path = str(imgdir) + str("//") + str(imgList[i])
        image = Image.open(img_path)
        # 输出维度
        print("RGB图像的维度：", np.array(image).shape)
        # 显示原图
        # RGB转换我灰度图像
        image_transforms = transforms.Compose([
            transforms.Grayscale(1)
        ])
        image = image_transforms(image)
        # 显示灰度图像
        image.save(img_path)




if __name__ == '__main__':
    image_RGB2Gray("G:\my secret\学习\研1\ocr\colour\\test")