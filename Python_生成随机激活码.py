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
    for x in range(1，count+1):
        print('第%s个激活码为：%s'%(i,getcode(length)))

loop(11,5)
"""
# -*- coding: utf-8 -*-
import random,string
from PIL import Image,ImageDraw,ImageFilter,ImageFont


def rand_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rand_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def graph(length):
    # 定义图层的宽度和高度
    width = 240
    height = 60
    # 新建一个白底图层，
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 设置字体类型
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
    # 进行画图,创建一个画笔
    draw = ImageDraw.Draw(image)
    # 遍历x，y，可组成一个宽度为x，高度为y的长方形
    for x in range(width):
        for y in range(height):
            # 画图，并填充图形
            draw.point((x, y), fill=rand_color())

    # 定义一个空字符result
    result = ''
    # 生成包含数字，大小写的字母的字符串集
    s=string.ascii_letters+string.digits

    for i in range(length):
        # 随机提起n位的字符串
        result +=s[random.randint(0,len(s)-1)]
    print('验证码数值为：',result)
    # 随机生成四个字符，draw.text()写进内容
    for t in range(length):
        draw.text((60 * t + 10, 10), result[t], font=font, fill=rand_color2())
    # 设置图像为模糊
    image = image.filter(ImageFilter.BLUR)
    # 保存图片
    image.save('newPicture.jpg', 'jpeg')


if __name__ == '__main__':
    length =4
    graph(length)

