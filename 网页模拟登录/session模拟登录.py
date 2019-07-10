def table(request, requestid):
    # 创建一个session对象，session可以帮助我们自定完成cookie的存储和发送
    session = requests.session()

    """
    1.请求登陆页面cookie
    2.发生登陆的post请求, 将用户名密码放在请求体中, cookie放在请求头中
    """
    # 账号密码登录的网页地址
    # login_url = "xxxxxx"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    # res1 = session.get(login_url, headers=headers)

    # print(res1.status_code)

    # 用户未登录时保存cookie
    # login_cookie = res1.cookies.get_dict()
    # print(login_cookie)
    
    # data表单中包含POST登录网页时所需的各种变量
    datas = {
        "loginfile": "/wui/theme/ecology8/page/login.jsp?templateId=2&logintype=1&gopage=",
        "logintype": 1,
        "fontName": "微软雅黑",
        "message": "",
        "gopage": "",
        "formmethod": "post",
        "rnd": "",
        "serial": "",
        "username": "",
        "isie": False,
        "islanguid": 7,
        "loginid": 账号,
        "userpassword": 密码,
        "submit": "登录"
    }

    """
    进行异常处理，判断是否模拟登录成功
    """
    try:
        # 通过抓包或chrome开发者工具分析得到登录的请求头信息，找到Referer（引用）：http://192.168.5.36:8081/login/VerifyLogin.jsp
        res2 = session.post("填写POST_url的目标网页",
                            headers=headers,
                            data=datas,
                            # 是否允许自动重定向
                            allow_redirects=False)
        if res2.status_code == 200:
            print('模拟登陆成功')
        else:
            print('出现错误，再接再厉')
    except RequestException:
        return None

    # 用户登录成功后的cookie
    # user_cookie = res2.cookies.get_dict()
    # print(user_cookie)
    
    # 找另一个进行目标进行爬取操作
    url = "xxxxxxx?requestid={}".format(requestid)

    # 访问目标主页
    res3 = session.get(url, headers=headers)
    print('目标主页：requestid={}的状态码为{}'.format(requestid, res3.status_code))

    html = res3.content
    doc = pq(html)
    items = doc.find('table').html()
    print(items)
