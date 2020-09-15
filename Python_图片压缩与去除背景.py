# -*- coding:utf-8 -*-
from __future__ import absolute_import
import requests
import logging
import os
import os.path
from PIL import Image
import time
import random
import glob
from tqdm import tqdm

# from removebg import RemoveBg # 官方类的调用


"""
爬坑：
    1. 先使用convert函数调整为目标尺寸
    2. 再使用remove_bg函数去除背景
    3. 严格按照这种顺序，不然会使得png背景变为黑色

问题：
    1. 使用官方的类，会使得去掉背景后的图片与源图片保存在同一个文件夹里，无法自定义输出路径
    2. 新图片命名很是不太规范，看起来好别扭
决定重写官方API: https://www.remove.bg
"""

API_ENDPOINT = "https://api.remove.bg/v1.0/removebg"


# 重写RemoveBg官方API
class RemoveBg(object):

    def __init__(self, api_key, error_log_file):
        """
        :param api_key: apiKey
        :param error_log_file: 日志文件
        """
        self.__api_key = api_key
        logging.basicConfig(filename=error_log_file)

    def remove_background_from_img_file(self, img_file_path, pic_title, out_dir, size="regular", bg_color=None):
        """
        Removes the background given an image file and outputs the file as the original file name with "no_bg.png"
        appended to it.
        :param pic_title: 图片标题且不带有存储格式后缀
        :param out_dir: 图片保存目录
        :param img_file_path: the path to the image file
        :param size: the size of the output image (regular = 0.25 MP, hd = 4 MP, 4k = up to 10 MP)
        """
        # Open image file to send information post request and send the post request
        img_file = open(img_file_path, 'rb')
        response = requests.post(
            API_ENDPOINT,
            files={'image_file': img_file},
            data={
                'size': size,
                'bg_color': bg_color
            },
            headers={'X-Api-Key': self.__api_key})
        response.raise_for_status()
        # 图片下载方式一：
        # if str(out_dir).endswith("/") or str(out_dir).endswith("\\"):
        #     self.__output_file__(response, out_dir + pic_title + ".png")
        # else:
        #     self.__output_file__(response, out_dir + "/" + pic_title + ".png")

        # 图片下载方式二：
        self.__output_file__(response, os.path.join(out_dir, pic_title + ".png"))

        # Close original file
        img_file.close()

    def __output_file__(self, response, new_file_name):
        # If successful, write out the file
        if response.status_code == requests.codes.ok:
            with open(new_file_name, 'wb') as removed_bg_file:
                removed_bg_file.write(response.content)
        # Otherwise, print out the error
        else:
            error_reason = response.json()["errors"][0]["title"].lower()
            logging.error("Unable to save %s due to %s", new_file_name, error_reason)


# 将压缩与去背景进行封装
class RemoveAndResize(object):
    def __init__(self, key):
        self.appKey = key

    # The Function Of Compress-Image
    @staticmethod
    def convert_jpg(file, outDir, width=258, height=441):  # self-defined this size of images
        img = Image.open(file)
        try:
            new_img = img.resize((width, height), Image.BILINEAR)
            if new_img.mode == 'P':
                new_img = new_img.convert("RGB")
            if new_img.mode == 'RGBA':
                new_img = new_img.convert("RGB")
            new_img.save(os.path.join(outDir, os.path.basename(file)))
        except Exception as e:
            print(e)

    # 图片压缩函数
    def resizeImage(self):
        for pic in tqdm(glob.glob("C:/Users/CHD/Desktop/images/*.jpg"), ncols=60):  # 目标文件的地址,好像必须要正则
            try:
                # self-defined the output of compress-image
                self.convert_jpg(pic, outDir="D:\data\images_deal\images_out")
            except Exception as e:
                print(e)
                continue

    def remove_bg(self):
        # 图片源地址
        path = "./images_in"
        # 图片输出路径
        out_path = "./images_demo"
        # appKey
        bg = RemoveBg(self.appKey, "error.log")
        for pic in os.listdir(path):
            try:
                time.sleep(random.random())
                print("==========正在处理：{} ========".format(pic))
                # 开始传参，调用函数
                bg.remove_background_from_img_file(img_file_path="{}/{}".format(path, pic),
                                                   pic_title=pic[:-4],  # 当后缀名有五位或以上时（如 .jpeg），需要自适应变化
                                                   out_dir=out_path,
                                                   bg_color="white")

            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    RAR = RemoveAndResize("BnWT7AWWsR5KZx4rAPpJkpAM")
    # RAR.resizeImage()
    RAR.remove_bg()
