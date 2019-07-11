# 按你输入的关键字（查询条件，保存的页数）
import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq


def get_url(city, month):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Cookie': 'td_cookie=1448616368; td_cookie=1444821621; td_cookie=104320322; bdshare_firstime=1561451297153; Hm_lvt_f48cedd6a69101030e93d4ef60f48fd0=1561451296,1562745245; __51cke__=; ASP.NET_SessionId=13f4ky55453b5045g04wcj45; __tins__4560568=%7B%22sid%22%3A%201562745245138%2C%20%22vd%22%3A%206%2C%20%22expires%22%3A%201562747449797%7D; __51laig__=6; Hm_lpvt_f48cedd6a69101030e93d4ef60f48fd0=1562745650',
        'Host': 'www.tianqihoubao.com'
    }

    base_url = 'http://www.tianqihoubao.com/lishi/taihu/month/201101.html'.format(city, month)
    try:
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('error,try again!!')
        # get_url(city, month)


def parse_url(html):
    # pyquery初始化对象
    doc = pq(html)
    # 找出该月份总共的天数
    num = int(doc('table tr').size())
    # 循环遍历每一天
    for i in range(0, num):
        """
        了解主目录：table标签下包含num个tr标签（一个tr标签表示一天），然后在find('tr')，tr标签下的每一个td标签表示日期，天气状态，气温，风力风向
        """
        riqi = doc.find('table tr').eq(i).find('td').eq(0).text()
        tianqizhuangtai = doc.find('table tr').eq(i).find('td').eq(1).text()
        qiwen = doc.find('table tr').eq(i).find('td').eq(2).text()
        fenglifengxiang = doc.find('table tr').eq(i).find('td').eq(3).text()
        with open('天气预报.txt', 'a') as f:
            f.write(riqi + ' ' + tianqizhuangtai + ' ' + qiwen + ' ' + fenglifengxiang + '\n')
        print(riqi, tianqizhuangtai, qiwen, fenglifengxiang)


def main():
    print('请输入查询关键字（比如chengdu）:', end=' ')
    city = input()
    print('请输入你所查询的日期（比如201405）:', end=' ')
    month = input()
    html = get_url(city, month)
    # print(html)
    parse_url(html)


if __name__ == '__main__':
    main()
