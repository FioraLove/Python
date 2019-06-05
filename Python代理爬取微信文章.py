# 爬取微信文章
import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from multiprocessing import Pool
from pyquery import PyQuery as pq

base_url = 'https://weixin.sogou.com/weixin?'

# headers即为cookies，host，User-Agent，Upgrade-Insecure-Requests
headers = {
    'Cookie': 'PLOC=CN3310; SUV=00774CBADA4B01BA5CF772A0EA802657; SUID=BA014BDA6C39980A000000005CF772A0; ABTEST=0|1559720704|v1; SNUID=F64D00964C4EC1C58DC36BCE4C5CD8AF; weixinIndexVisited=1; JSESSIONID=aaaafPuUjjTnC6WfwrkRw; sct=2',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
# 使用代理来处理我们被反爬虫封锁的ip

"""获取代理值方法：点击pycharm的Terminal终端，输入： cd ../ProxyPool
再输入：python3  文件名.py
"""
proxy_pool_url = ''  # 代理值
proxy = None
max_count = 5  # 最大请求次数


# 判断代理是否起作用
def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text

        return None
    except ConnectionError:
        return None


def get_html(url, count=1):
    global proxy  # 定义一个全局的代理，以免一直重复打印
    if count >= max_count:  # 判断是否请求次数过多
        print('trying too much')

    try:  # 做一个异常处理，若状态码为302，则再发起请求

        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }

            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)

        if response.status_code == 200:
            return response.text
        if response.status_code == 302:

            # return response.text

            print('302')
            proxy = get_proxy()
            if proxy:
                print('using proxy', proxy)
                return get_html(url)
            else:
                print('get proxy faild')
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url)


keyword = '风景'


def get_index(keyword, page):
    # data数据在Network中的最后一个Query String parameters中寻找
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)  # urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
    url = base_url + queries  # 拼接成一个完整的url
    html = get_html(url)  # 调用函数get_html,参数现在为完整的URL，request.get(url)获取网页的源代码
    return html


# 解析索引页
def parse_index(html):
    doc = pq(html)
    items = doc('')
    for item in items:
        yield item.attr('href')


def main():
    for page in range(2, 101):
        html = get_index(keyword, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                print(article_url)


if __name__ == '__main__':
    # get_index('风景',2)  # 输入两个查询参数，关键字：风景，页数：第2页
    main()
    pool = Pool()
