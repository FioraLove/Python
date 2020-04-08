"""
    需求：
        就是设计一个爬虫，给功能如下，
        1.抓取网页上关于光电企业信息（岗位，各岗位的薪资、技能要求、工资、地点等信息）
        2.将这些信息存入数据库
        3.对数据库的数据进一步分析，提炼，并将信息转换为散点图和柱状图，并加入了tkinter图形操作界面
    ps:拉钩网的cookie很容易失效，所以要特别注意
"""
import json
import time
import requests
from tqdm import tqdm

# 1.1、先爬取拉勾的数据,是一个ajax动态加载的网站
headers = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E5%85%89%E7%94%B5?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

target_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"


def get_lagou_cookie():
    # 原始网页的URL
    url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    s = requests.session()
    s.get(url, headers=headers, timeout=3)  # 请求首页获取cookies
    cookies = s.cookies  # 为此次获取的cookies
    cookie_dict = s.cookies.get_dict()
    print(requests.utils.dict_from_cookiejar(s.cookies))
    with open("./getDictCookie.json", 'w', encoding="utf-8") as f:
        f.write(json.dumps(cookie_dict))
    print(cookie_dict)
    print(cookies)
    return cookies


def get_lagou_url(url, page, cookies, kw):
    json = {
        'first': 'true',
        'pn': str(page),
        'kd': str(kw)
    }

    try:
        response = requests.post(url=url, headers=headers, data=json, cookies=cookies)
        if response.status_code == 200:
            # json返回数据，数据是一个数组
            html = response.json()['content']['positionResult']['result']
            content = ""
            for i in range(len(html)):
                name = (str(html[i]['positionName']))  # 职位名称
                fullName = (str(html[i]['companyFullName']))  # 公司全名
                companySize = (str(html[i]['companySize']))  # 公司规模
                financeStage = (str(html[i]['financeStage']))  # 是否融资
                position = (str(html[i]['positionAdvantage']))  # 公司福利
                label = (str(html[i]['positionLables']))  # 能力要求
                createTime = (str(html[i]['createTime']))  # 发布时间
                district = (str(html[i]['city'] + html[i]['district']))  # 具体的地址
                salary = (str(html[i]['salary']))  # 薪资
                workYear = (str(html[i]['workYear']))  # 工作经验
                education = (str(html[i]['education']))  # 学历要求
                content += name + "  " + fullName + "  " + companySize + "  " + financeStage + "  " + position + "  " + \
                           label + "  " + createTime + "  " + district + "  " + salary + "  " + workYear + "  " + education + "\n"
            with open("./a.txt", "w", encoding="utf-8") as f:
                f.write(content)

    except Exception as e:
        print(e)


def get_many_page(cookies):
    # 实现多页请求
    page = int(input("请输入查询目标页数："))
    kw = str(input("请输入查询相关内容："))
    for i in tqdm(range(1, page + 1)):
        get_lagou_url(target_url, i, cookies=cookies, kw=kw)
        time.sleep(10)


if __name__ == '__main__':
    cookie = get_lagou_cookie()
    get_many_page(cookie)
