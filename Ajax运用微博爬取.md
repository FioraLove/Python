from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq

base_url='https://m.weibo.cn/api/container/getIndex?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'https://m.weibo.cn/u/2830678474'
}

def get_page(page):
    params={
        'value':'2830678474',
        'type':'uid' ,
        'containerid': '1076032830678474',
        'page':page
    }
    url= base_url+urlencode(params)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException as e:
        print('error',e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo={}
            weibo['id']=item.get('id')
            weibo['text']=pq(item.get('text')).text()
            weibo['attitudes']=item.get('comment_count')
            weibo['reposts']=item.get('resport_count')
            yield weibo

if __name__ == '__main__':
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
