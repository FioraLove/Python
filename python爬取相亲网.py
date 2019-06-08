import requests
import os

from requests.exceptions import RequestException


def query_age():
    age = int(input("your age:"))
    if 21 <= age <= 30:
        startage = 21
        endage = 30
    elif 31 <= age <= 40:
        startage = 31
        endage = 40
    else:
        startage = 0
        endage = 0
    return startage, endage


# 性别
def query_sex():
    sex = input('your sex:')
    if sex == '男':
        gender = 1
    else:
        gender = 2
    return gender


def query_money():
    money = int(input('请输入期望的对方薪资（如;8000):'))
    if 2000 <= money < 5000:
        salary = 2
    if 5000 <= money < 10000:
        salary = 3

    if 10000 <= money < 20000:
        salary = 4

    if 20000 <= money:
        salary = 5

    return salary


def query_data():
    # 年龄
    startage, endage = query_age()
    # 性别
    gender = query_sex()
    # 薪资
    salary = query_money()

    for page in range(1, 11):
        # 解析网站
        json = get_one(page, startage, endage, gender, salary)
        # items=json['data','list']
        for item in json['data']['list']:
            save_image(item)


def save_image(item):
    if not os.path.exists('images'):
        os.mkdir('images')
    image_url = item['avatar']
    response = requests.get(image_url)
    if response.status_code == 200:
        file_path = 'image/{}.jpg'.format(item['username'])
        if not os.path.exists(file_path):
            print("正在获取：%s的信息" % item['username'])
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print('已经下载过来！')


def get_one(page, startage, endage, gender, salary):
    # 请求头
    headers = {
        'Referer': 'http://www.7799520.com/jiaoyou.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Cookie': 'Hm_lvt_ee0de768b7db1b355930288073352dbe=1559992142; 59167___602875_KS_59167___602875=15937b459ed24af8878e9e9547886d85; 59167___602875_KS_ri_ses=19037863024%7C2A2CE69BB05E689C07E43624C529CF3B-null; Hm_lpvt_ee0de768b7db1b355930288073352dbe=1559992393; 59167___602875_curPageNum=35; 59167___602875_curRanId=1559994533040_1559992393627; 59167___602875_curPage_1559992393627=35_true_1559994533041',
    }

    base_url = 'http://www.7799520.com/api/user/pc/list/search?startage={}&endage={}&gender={}&marry=1&lunar=1&education=40&salary={}&page={}'.format(startage, endage, gender, salary, page)
    # print(base_url)
    while True:
        try:
            response = requests.get(base_url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except RequestException:
            print('badwoman')
            return None


query_data()
