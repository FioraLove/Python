import hashlib

m = hashlib.md5()
m.update('陈浩东'.encode('utf-8'))
print(m.hexdigest())
base_name = m.hexdigest()
m1 = hashlib.md5()
m1.update('chen15867119504,'.encode('utf-8'))
base_password = m1.hexdigest()


def get_code(input_content):
    m = hashlib.md5()
    m.update(input_content.encode('utf-8'))
    return m.hexdigest()


def main():
    name = input('请输入你的姓名：')
    password = input('请输入你的密码：')
    if get_code(name) != base_name:
        print('this name is error!')
    else:
        if get_code(password) != base_password:
            print('this password is error')
        else:
            print('great! all is right！')
            print('欢迎进入Pycharm！')


if __name__ == '__main__':
    main()
