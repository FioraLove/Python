# -*- coding:utf-8 -*-
import requests
import time
import random
from tqdm import tqdm
from threading import Thread

""""
# 保存成txt格式版

# 定于一个装饰器
def start_t(func):
    def inner(*args, **kwargs):
        for i in range(4):
            response = []
            for j in range(25):
                response.append(func(*args, **kwargs))
            content = "".join(response)
            # 每执行25次函数后将结果写入txt文件
            with open("./a.txt", "a+", encoding="utf-8") as f:
                f.write(content)
    return inner()


@start_t
def get_info_1():
    url = "https://s.nmsl8.club/getloveword?type=2"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "referer": "https://s.nmsl8.club/loveword?type=2",
        "x-csrf-token": "SJoNf6r3hhcqe0TYsMArfcH6lth6L2htr14ZiruL",
        "x-requested-with": "XMLHttpRequest"
    }
    session = requests.Session()
    try:
        response = session.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            level = random.randint(1, 4)
            # 写入txt文件
            content = str(level) + "\t" + data["content"] + "\t\n"
            time.sleep(random.random())
            return content

    except Exception as e:
        print(e)


@start_t
def get_info_2():
    url = "https://s.nmsl8.club/getloveword?type=2"
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "referer": "https://s.nmsl8.club/loveword?type=2",
        "x-csrf-token": "SJoNf6r3hhcqe0TYsMArfcH6lth6L2htr14ZiruL",
        "x-requested-with": "XMLHttpRequest"
    }
    session = requests.Session()
    try:
        response = session.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            level = random.randint(1, 4)
            # 写入txt文件
            content = str(level) + "\t" + data["content"] + "\t\n"
            time.sleep(random.random())
            return content
    except Exception as e:
        print(e)


if __name__ == '__main__':
    time1 = time.time()
    t1 = Thread(target=get_info_1, args=())
    t2 = Thread(target=get_info_2, args=())
    t1.start()
    t1.join()
    t2.start()
    print("总耗时：", time.time()-time1)
"""

# 通过API接口保存数据版本
# 定于一个装饰器
def start_t(func):
    def inner(*args, **kwargs):
        session = requests.Session()
        for i in tqdm(range(50)):
            url = "http://127.0.0.1:8001/nmsl/ndsl/10/?offset=0&limit=3"
            level, content = func(*args, **kwargs)
            data = {
                "level": int(level),
                "content": str(content)
            }
            try:
                response = session.post(url=url, data=data, timeout=6)
                if response.status_code != 200:
                    continue
            except Exception as e:
                print(e)

    return inner()


@start_t
def get_info_1():
    url = "https://s.nmsl8.club/getloveword?type=2"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "referer": "https://s.nmsl8.club/loveword?type=2",
        "x-csrf-token": "SJoNf6r3hhcqe0TYsMArfcH6lth6L2htr14ZiruL",
        "x-requested-with": "XMLHttpRequest"
    }
    session = requests.Session()
    try:
        response = session.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            level = random.randint(1, 4)
            # 写入txt文件

            time.sleep(random.random())
            return level, data["content"]

    except Exception as e:
        print(e)


@start_t
def get_info_2():
    url = "https://s.nmsl8.club/getloveword?type=2"
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "referer": "https://s.nmsl8.club/loveword?type=2",
        "x-csrf-token": "SJoNf6r3hhcqe0TYsMArfcH6lth6L2htr14ZiruL",
        "x-requested-with": "XMLHttpRequest"
    }
    session = requests.Session()
    try:
        response = session.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            level = random.randint(1, 4)
            # 写入txt文件

            time.sleep(random.random())
            return level, data["content"]
    except Exception as e:
        print(e)


if __name__ == '__main__':
    time1 = time.time()
    print(time1)
    t1 = Thread(target=get_info_1, args=())
    t2 = Thread(target=get_info_2, args=())
    t1.start()
    t1.join()
    t2.start()
    print(time.time())
    print("总耗时：", time.time() - time1)
