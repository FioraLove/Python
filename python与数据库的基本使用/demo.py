import cx_Oracle
import re
import requests
from requests.exceptions import RequestException

# 创建与数据库的链接（需要在电脑上安装数据库，并创建名为db的数据库，在创建表的相关列
db = cx_Oracle.connect('spider/spider@127.0.0.1:3306/Tables')
# 创建一个游标，查询数据库
cursor = db.cursor()
# 查询所有数据
cursor.execute('select * from TEST')
print(cursor.fetchall())


# 发送请求，获取网页的url
def get_url(page):
    url = 'http://www.doutula.com/photo/list/?page={}'.format(page)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('error')
    return None


# 解析网页内容，正则获取每一张图片的URL以及title
def parse_page(html):
    pattern = re.compile(r'data-original="(.*?)" alt="(.*?)" class=', re.S)
    imageList = re.findall(pattern, html)
    # 循环遍历元组
    for item in imageList:
        image_url = item[0]
        title = item[1]
        # 插入数据到数据库
        cursor.executc('insert into TEST(`title`,`image_url`)values(`%s`,`%s`)' % (title, image_url))
        print('正在保存%s' % title)
        # 提交到数据库
        db.commit()
        # 打印图片的title以及图片的URL
        print(title, image_url)


def main(page):
    # 从第一页开始抓取
    for i in range(1, page + 1):
        html = get_url(page)
        parse_page(html)


if __name__ == '__main__':
    main(2)
