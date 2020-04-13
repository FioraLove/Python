import requests
import random
import re
import json
import time


def open_json():
    # 读取代理池
    with open("./proxies_pool.json", 'r', encoding="utf-8") as f:
        proxy_arrays = json.loads(f.read())
    return proxy_arrays


# 获取json数据格式里的数据
proxies_array = open_json()
# 获取代理数组
proxy_array = proxies_array["https"]


def get_proxy():
    # 程序休眠5秒，减缓接口调用速度
    time.sleep(2)
    # 判断数组代理池是否为空
    if len(proxy_array) > 0:

        # 随机获取某个代理
        proxy_random = random.choice(proxy_array)
        print("代理池的随机代理：", proxy_random)
        # 判断代理是否可用
        try:
            Proxies = {
                "https": proxy_random
            }
            response = requests.get(url="http://icanhazip.com/", timeout=8, proxies=Proxies)
            proxyIP = response.text
            print("http://icanhazip.com/测试后的代理返回值：", proxyIP.replace("\n", ""))

            # 将返回后的代理IP进行处理
            a = proxyIP.replace('.', '').replace('\n', '')
            # 将代理池里随机取出的代理进行处理
            b = re.findall('//(\d+\.\d+\.\d+\.\d+):', proxy_random)[0].replace('.', '')

            # 将两个IP进行对比
            if int(a) == int(b):
                print("代理IP:'" + proxyIP + "'有效！")
                proxy_return = {
                    "https": str(proxy_random)
                }
                # 如果两个代理相同，表示代理有效
                return proxy_return
            else:
                print("\033[0;44;42m返回不是代理池中的ip，代理IP无效！继续执行！！！\033[0m")
                # 如果随机代理测试无效就从代理池中删除
                proxy_array.remove(str(proxy_random))
                # 从代理池中删除无效代理后，递归执行验证模块
                get_proxy()
        except Exception as e:
            print(e)
            print("\033[0;44;42m 代理IP无效！\033[0m", e)
    else:
        print("\033[0;44;42m IP代理池为空，请重新添加！\033[0m")
        return None


def save_json():
    # 获取经过检验后可行的代理数组
    proxy_tested = proxy_array
    PROXIES_NEW = {
        "https": proxy_tested
    }
    with open('./proxies_pool.json', 'w', encoding='utf-8')as f:
        f.write(json.dumps(PROXIES_NEW))


if __name__ == '__main__':
    proxies = get_proxy()
    print("有效代理： ", proxies)
    save_json()
