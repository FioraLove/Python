#半自动爬虫，需要先保存为TXT文件
import re
target = "http://www.jikexueyuan.com/course/android/?pageNum=2"
total_page = 20

# 打开文件，并read（），其中可能会遇到编码错误，利用encoding="utf-8"
f = open('text.txt','r',encoding="utf-8")
html = f.read()

f.close()

# 利用正则表达式的search（）方法
# 【当搜索内容只有一个时，使用search更快，因为findall会遍历全部内容后才停止】
# group（n）表示常用符号(.*?)使用几次就填写几次，必不可少，没有写0；
title = re.search('<title>(.*?)</title',html,re.S).group(1)
print (title)

# 利用findall找出全部的链接，注意re.S一定要有
links = re.findall('href="(.*?)"',html,re.S)
for each in links:   # 打印出所有的链接
    print(each)

# 先抓大，在抓小思想
text_fied = re.findall('<ul>(.*?)</ul',html,re.S)[0]
the_text = re.findall('">(.*?)</a>',text_fied,re.S)
for every_text in the_text:
    print(every_text)

# sub实现翻页功能
for i in range(2,total_page+1):  #range()函数左闭右开
    new_links = re.sub('\d+','pageNum=%d'%i,target,re.S)
    print(new_links)


