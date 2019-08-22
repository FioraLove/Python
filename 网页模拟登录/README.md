### Cookie的使用：

    # -*- coding:utf-8 -*-
    import requests
    import os
    import json

    """
    三种Cookie请求方式:
    第一种：cookie放在headers中
    第二种：cookie字典传给cookies参数
    第三种：先发送post请求，获取cookie，带上cookie请求登陆之后的页面
    """

    # cookie的读取(先判断cookie文件是否存在，若存在直接读取填入headers中，若不存在，则需要模拟登录后保存cookie)
    COOKIE_PATH = 'xxx.json'
    # to check whether it exist
    if os.path.exists(COOKIE_PATH):
        # to load the file of cookie
        with open(COOKIE_PATH, 'r') as f:
            cookie_ct = json.loads(f)

        headers = {
            'User-Agent': 'xxxxxx',
            'Host': 'www.baidu.com',
            'Cookie': cookie_ct,
        }
        try:
            # try to load some website
            session = requests.session()
            response = session.get(url='www.baidu.com', headers=headers, timeout=0.1)
            if response.status_code == 200:
                print(response.content)
        except Exception as e:
            print(e)

    """
    assume the cookie is not existing:
    so,we need to send request_POST ,and get the cookies,
    finally,we should load the website with the cookies 
    """
    headers = {
        "User-Agent": 'dddddddd',
    }
    session = requests.session()
    # the post_url can be found in the form or capture the url
    post_url = 'http://www.renren.com/PLogin.do'
    data = {
        'name': 'chd',
        'age': 18,
        'password': 'chen111',
    }
    res = session.post(url=post_url, headers=headers, data=data, timeout=0.1)
    # 请求失败抛出
    if (res.status_code != 200):
        raise Exception("登录失败！")

    # 获取cookie
    cookies_ct = requests.utils.dict_from_cookiejar(session.cookies)
    # 将cookie保存至本地文件
    with open(COOKIE_PATH, "w") as f:
        json.dump(cookies_ct, f)
