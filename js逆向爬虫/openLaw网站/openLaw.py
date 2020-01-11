import re
import requests
import execjs

# 请求登录url
url = "http://openlaw.cn/login"
headers = {
    "Origin": "http://openlaw.cn",
    "Referer": "http://openlaw.cn/login.jsp",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}


# 先请求一次网页，获取页面中的csrf
def get_csrf():
    try:
        csrfUrl = "http://openlaw.cn/login.jsp?$=deny"
        session = requests.session()
        response = session.get(csrfUrl, headers=headers, timeout=5)
        if (response.status_code == 200):
            pattern = re.compile('name="_csrf" value="(.*?)"/>', re.S)
            result = re.findall(pattern, response.text)
            return result

    except Exception as e:
        print(e)


def get_pwd():
    with open('main.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    # 编译js函数
    ctx = execjs.compile(js_code)
    # 执行js中的getPassword函数，参数为password
    result = ctx.call('getPassword', 'a123456')
    return result


# 登录openLaw网站
def login():
    data = {
        "_csrf": (get_csrf())[0],
        "username": "badwoman",
        "password": get_pwd(),
        "_spring_security_remember_me": "true"
    }
    try:
        # 模拟登录openLaw
        response = requests.post(url=url, headers=headers, data=data, timeout=5)
        if (response.status_code == 200):
            return response.text
        return None
    except Exception as e:
        print(e)


if __name__ == '__main__':
    login()
