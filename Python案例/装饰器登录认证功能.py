import os

# 写一个验证登录的装饰函数
login_status = False

# 定义一个装饰器函数。参数为被装饰的函数的内存地址（即函数名）
def login(fun):
    # 判读用户信息的文件是否存在
    file = os.path.exists('user_info.txt')
    # 若文件存在
    if file is True:
        with open('user_info.txt', 'r+', encoding='utf-8') as f:
            # eval 1.返回表达式的值 2.txt文件读取为字典
            user_info = eval(f.read())

    else:
        choice = input("是否注册用户？[Y/N]")
        if choice == 'Y' or choice == 'N':
            name = str(input("请输入新用户用户名："))
            password = str(input("请输入新用户密码："))
            user_info = {'name': name, 'password': password}

        with open('user_info.txt', 'w', encoding='utf-8') as f:
            # f.wwrite()仅能写入str型数据
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
        # 可以运用嵌套函数，在login中再定义一层。
        # 重点处：该代码表示实现被装饰函数的功能
            fun()
    # 重点处：login只返回里层函数的函数名，下次执行被装饰函数时再调用里层函数。
    return logind


# 写一个计时统计的装饰函数
import time


def time_total(func):
    def inner():
        start = time.time()
        func()
        wait_time = time.time() - start
        print("%s 运行时间:" % func.__name__, wait_time)

    return inner


a = time.localtime()


@time_total
def log_1():
    print('%s-%s-%s:\n' % (a.tm_year, a.tm_mon, a.tm_mday))


@time_total
def log_2():
    time.sleep(2)
    print('%s-%s-%s:\n' % (a.tm_year, a.tm_mon, a.tm_mday))


@login
def log_3():
    time.sleep(4)
    print('%s-%s-%s:' % (a.tm_year, a.tm_mon, a.tm_mday))


log_1()
log_2()
log_3()

# 装饰器一般格式：
