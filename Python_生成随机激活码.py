"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
"""
import random,string

def getcode(length):
    result = ''  #创建空字符串
    s = string.ascii_letters + string.digits  # 获取所有字母（大小写）和数字
    for i in range(length):
        str = s[random.randint(0,len(s)-1)]  # 随机生成字符
        result +=str  # 生成的字符储存在result中
    return result


def loop(length,count):
    for x in range(count):
        print(getcode(length))

loop(11,5)
"""
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string


# 生成随机字母，数字的字符串
def getcode(length):
    result = ''  # 创建空字符串
    s = string.ascii_letters + string.digits  # 获取所有字母（大小写）和数字
    for i in range(length):
        str = s[random.randint(0, len(s) - 1)]  # 随机生成字符
        result += str  # 生成的字符储存在result中
    return result


# 随机生成图片的RGB（a,b,c,）三个值都是random.randint(64,255)
def rand_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 再随机生成图片的RGB（a,b,c,）三个值都是random.randint(32,127)
def rand_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 定义图层的宽度和高度
width = 240
height = 60
# 新建一个白底图层，
image = Image.new('RGB', (width, height), (255, 255, 255))
# 设置字体类型
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# 进行画图
draw = ImageDraw.Draw(image)
# 遍历x，y，可组成一个宽度为x，高度为y的长方形
for x in range(width):
    for y in range(height):
        # 画图，并填充图形
        draw.point((x, y), fill=rand_color())
# 随机生成四个字符，draw.text()写进内容
for t in range(4):
    draw.text((60 * t + 10, 10), getcode(1), font=font, fill=rand_color2())
# 设置图像为模糊
image = image.filter(ImageFilter.BLUR)
# 保存图片
image.save('newPicture.jpg', 'jpeg')

