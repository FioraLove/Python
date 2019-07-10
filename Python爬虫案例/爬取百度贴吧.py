# 按你输入的关键字（查询条件，保存的页数）
import requests
from requests.exceptions import RequestException
import re
from pyquery import PyQuery as pq


def get_url(kw, pn):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Host': 'tieba.baidu.com'
    }

    base_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(kw, pn)
    try:
        response = requests.get(base_url, headers=headers, timeout=1.2)
        if response.status_code == 200:
            return response.content
        return None
    except RequestException:
        print('error,try again!!')
        get_url(kw, pn)


def parse_url(kw, pn):
    html = get_url(kw, pn)
    doc = pq(html)
    # 获取每一个用户所评论信息
    pattern1 = re.compile('<div class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>', re.S)
    response = re.findall(pattern1, html)
    print(type(response))


def main():
    print('请输入查询关键字,输入格式如:英雄联盟')
    kw = input()
    pn = int(input('请输入你所查询的贴吧页数:'))
    for i in range(0, pn):
        pn = 50 * i
        with open('第{}页.html'.format(i), 'wb') as f:
            f.write(get_url(kw, pn))


if __name__ == '__main__':
    main()
