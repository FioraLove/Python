import pymysql
import re
import requests
from requests.exceptions import RequestException

# 创建与数据库的链接（需要在电脑上安装数据库，并创建名为db的数据库，在创建表的相关列
db - pymysql.connect(host - '127.0.0.1', port - 3306, db - 'db', user - 'root', password - 'root', charset='utf8')
# 创建一个游标，查询数据库
cursor = db.cursor()
# 查询所有数据
cursor.execute('select * from image')
print(cursor.fetchall())


#
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


def parse_page(html):
    pattern = re.compile(r'data-original="(.*?)".*?alt="(.*?)"', re.S)
    imageList = re.findall(pattern, html)
    for item in imageList:
        image_url = item[0]
        title = item[1]
        # 插入数据到数据库
    cursor.executc('insert into image(`image_url`,`title`)' values('{}', '{}').format(image_url, title))
    print('正在保存%s' % title)
    # 提交到数据库
    db.commit()


html = get_url(1)
parse_page(html)

html = get_url(1)
parse_page(html)
