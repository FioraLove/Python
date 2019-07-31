# -*- coding:utf-8 -*-
"""
要求用户输入用户名和密码，要求密码长度不少于6个字符，且必须以字母开头，
如果密码合法，则将该密码使用md5算法加密后的十六进制概要值存入名为password.txt的文件，
超过三次不合法则退出程序
"""
import hashlib, json, re


def func():
    count = 0
    while count < 3:
        username = input('username:').strip()
        password = input('password:').strip()

        if len(password) < 6 or not re.search('\A([a-z]|[A-Z])', password):
            count += 1
            print('try again!!')

        else:
            # 创建hashlib对象
            new_md5 = hashlib.md5()
            # 将字符串载入到md5对象中，获得md5算法加密
            new_md5.update(password.encode('utf-8'))

            obj = {
                'username': username,
                # 通过hexdigest()方法，获得new_md5对象的16进制md5显示
                'password': new_md5.hexdigest()
            }
            with open('password.txt', 'a', encoding='utf-8') as f:
                f.write('\n' + json.dumps(obj))
            break


if __name__ == '__main__':
    func()
