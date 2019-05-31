"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
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

