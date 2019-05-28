# 爬取下载图片
import re
import requests
f = open('sources.txt','r',encoding='utf-8')
html = f.read()
f.close()

pic_url = re.findall('<a img src="(.*?)" ',html,re.S)
i = 0
for each in pic_url:
    print ('now downloading:'+each)
    pic = requests.get(each)
    fp = open('pic\\'+str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i +=1

