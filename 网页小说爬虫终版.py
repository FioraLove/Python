"""
网站首页的各个章节目录的URL是需要拼接的
"""

import requests
import re
import time
time1 = time.time()
# 下载一个网页
url = 'http://www.u33.cc/u105450/'
# 模拟浏览器发送http请求
response = requests.get(url)
# 编码方式
response.encoding ='utf-8'

# 目标小说的主页网页源代码
html = response.text
# 小说的名字
title = re.findall('<title>(.*?)</title>',html,re.S)[0]

# 新建一个文件，保存小说的内容
fb = open('%s.txt'%title,'w',encoding='utf-8')

# 获取每一章信息（章节，url）
dl = re.findall('<dl>(.*?)</dl>',html,re.S)[0]
chapter_info_list = re.findall('<a style="" href="(.*?)">(.*?)</a></dd>',dl)

# 循环每一章节，分别去下载
for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = "http://www.u33.cc/u105450/%s"%chapter_url

    #下载每一章节
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding='utf-8'
    chapter_html = chapter_response.text

    #提取章节内容
    chapter_content = re.findall('<div id="content">(.*?)<script',chapter_html,re.S)[0]


    # 清洗数据
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('&nbsp', '')
    chapter_content = chapter_content.replace('<br/>', '')


    #持久化
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url)

time2 = time.time()
print(time2-time1)


"""
下面的代码的各个章节目录的URL是完整的，不需要拼接
"""

import requests
import re
import time
from multiprocessing import Pool
time1 = time.time()
# 下载一个网页
url = 'https://www.biquge5.com/57_57544/'
# 模拟浏览器发送http请求
response = requests.get(url)
# 编码方式
response.encoding ='gbk'

# 目标小说的主页网页源代码
html = response.text
# 小说的名字
title = re.findall('<h1>(.*?)</h1>',html,re.S)[0]

# 新建一个文件，保存小说的内容
fb = open('%s.txt'%title,'w',encoding='utf-8')

# 获取每一章信息（章节，url）
dl = re.findall('<ul class="_chapter">(.*?)</ul>',html,re.S)[0]
chapter_info_list = re.findall('<a href="(.*?)">(.*?)</a>',dl)



# 循环每一章节，分别去下载
for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    print(chapter_url,chapter_title)
    #下载每一章节
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding='gbk'
    chapter_html = chapter_response.text

    #提取章节内容
    chapter_content = re.findall('<div id="content">(.*?)</div',chapter_html,re.S)[0]


    # 清洗数据
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace(';', '')
    chapter_content = chapter_content.replace('&nbsp', '')
    chapter_content = chapter_content.replace('<br/>', '')


    #持久化
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')


pool =Pool()
time2 = time.time()
print(time2-time1)
