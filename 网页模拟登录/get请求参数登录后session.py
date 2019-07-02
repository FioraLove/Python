import requests

# 创建会话
s = requests.Session()

# 登录要请求的地址，
url = "http://www.jokeji.cn/user/c.asp"
# 登录所需要的get参数
# 通过抓包的到需要传递的参数
data = {
    'u': '17312345678', # 账号
    'p': '123456', # 密码
    'sn': '1',
    't': 'big'
}
# 通过抓包或chrome开发者工具分析得到登录的请求头信息,
headers = {
    'Referer': 'http://www.jokeji.cn/User/Login.asp',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
# 开始登录
r = s.get(url=url, params=data, headers=headers)
print(r.text)


# 请求一个登录之后的页面
headers1 = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
url = 'http://www.jokeji.cn/User/MemberCenter.asp'
r = s.get(url=url, headers=headers1)
# 定制字符集
r.encoding = 'gbk'
# 显示内容
print(r.text)
