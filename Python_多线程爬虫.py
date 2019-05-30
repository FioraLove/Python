"""
多线程爬虫主要涉及知识点：
from multiprocessing.dummy import Pool as ThreadPool
pool = Pool(4)
results = pool.map()  # map(爬取函数，网址列表)
"""
from multiprocessing.dummy import Pool as ThreadPool

import requests

import time

def getsource(url):  # 定义函数，通过requests。get获取网页源代码
    html = requests.get(url)

urls = []

for i in range(1,21):  # 通过列表将网址添加到列表中
    newpage = 'https://tieba.baidu.com/p/3522395718?pn=' +str(i)
    urls.append(newpage)

time1 = time.time()
for i in urls:
    print(i)
    getsource(i)

time2 = time.time()
print("单线程耗时："+str(time2-time1))

pool = ThreadPool(4)
time3 = time.time()
results = pool.map(getsource,urls)
pool.close()
pool.join()
time4 = time.time()
print("并行耗时："+str(time4-time3))
