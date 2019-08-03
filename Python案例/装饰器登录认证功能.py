
import os,time
# 定义一个装饰器函数。参数为被装饰的函数的内存地址（即函数名）
login_status = False
def login(fun):
    # 判读用户信息的文件是否存在
    file = os.path.exists('user_info.txt')
    # 若文件存在
    if file is True:
        with open('user_info.txt', 'r+', encoding='utf-8') as f:
            # eval 1.返回表达式的值 2.txt文件读取为字典
            user_info = eval(f.read())

    else:
        # 使得输入的字符全部变为小写
        choice = input("是否注册用户？[Y/N]").lower()
        if choice == 'Y' or choice == 'y':
            name = str(input("请输入新用户用户名："))
            password = str(input("请输入新用户密码："))
            user_info = {'name': name, 'password': password}

            with open('user_info.txt', 'w', encoding='utf-8') as f:
                # f.write()仅能写入str型数据
                f.write(str(user_info))




    def logind():
        _username = user_info['name']
        _password = user_info['password']
        global login_status
        if login_status is False:
            username = input('username')
            password = input('password')
            if username == _username and password == _password:
                print('login succ')
                login_status = True
            else:
                print('the name or password is worng')
        if login_status:
            fun()

    return logind

a = time.localtime()

@login
def log_1():
    print('%s-%s-%s-%s-%s' % (a.tm_year, a.tm_mon, a.tm_mday,a.tm_min,a.tm_sec))

@login
def log_2():
    time.sleep(2)
    print('%s-%s-%s-%s-%s' % (a.tm_year, a.tm_mon, a.tm_mday,a.tm_min,a.tm_sec))

@login
def log_3():
    time.sleep(4)
    print('%s-%s-%s-%s-%s' % (a.tm_year, a.tm_mon, a.tm_mday,a.tm_min,a.tm_sec))


log_1()
log_2()
log_3()

