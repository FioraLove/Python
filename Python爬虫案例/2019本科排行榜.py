import requests, csv
from pyquery import PyQuery as pq
from requests.exceptions import RequestException


def get_url():
    url = 'http://www.ccutu.com/46264.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Host': 'www.ccutu.com'
    }
    try:
        response = requests.get(url=url, headers=headers, timeout=1.2)
        if response.status_code == 200:
            # 返回类型为content类型
            return response.content
        return None
    except RequestException:
        print('请求错误！')
        get_url()


def parse():
    html = get_url()
    doc = pq(html)
    num = int(doc('table tbody tr').size())
    for i in range(num):
        rank = doc.find('tr').eq(i).find('td').eq(0).text()
        name = doc.find('tr').eq(i).find('td').eq(1).text()
        point = doc.find('tr').eq(i).find('td').eq(2).text()
        loction = doc.find('tr').eq(i).find('td').eq(3).text()
        loction_rank = doc.find('tr').eq(i).find('td').eq(4).text()
        mold = doc.find('tr').eq(i).find('td').eq(5).text()
        mold_rank = doc.find('tr').eq(i).find('td').eq(6).text()
        print(rank, name, point, loction, loction_rank, mold, mold_rank)
        # 注意这里的encoding='utf-8'的格式转换
        with open('本科排名.csv', 'a', encoding='utf-8') as f:
            f.write(rank + ' ' + name + ' ' + point + ' ' + loction + ' ' + loction_rank + ' ' + mold + ' ' + mold_rank + '\n')


if __name__ == '__main__':
    html = get_url()
    parse()
