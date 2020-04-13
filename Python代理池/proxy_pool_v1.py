import requests
import random
import re
import json


def get_proxy():
    # 读取代理池
    with open("./proxies_pool.json", 'r', encoding="utf-8") as f:
        proxy_array = json.loads(f.read())

    # 获取代理数组
    proxy_array = proxy_array["https"]

    # 判断数组代理池是否为空
    if len(proxy_array) > 0:

        # 随机获取某个代理
        proxy_random = random.choice(proxy_array)
        print("代理池的随机代理：", proxy_random)
        # 判断代理是否可用
        try:
            proxies = {
                "https": proxy_random
            }
            response = requests.get(url="http://icanhazip.com/", timeout=8, proxies=proxies)
            proxyIP = response.text
            print("icanhazip测试后的代理返回值：", proxyIP)
            # 将返回后的代理IP进行处理
            a = proxyIP.replace('.', '').replace('\n', '')
            print("a:", a)
            # 将代理池里随机取出的代理进行处理
            b = re.findall('//(\d+\.\d+\.\d+\.\d+):', proxy_random)[0].replace('.', '')
            print("b：", int(b))
            # 将两个IP进行对比
            if int(a) == int(b):
                print("代理IP:'" + proxyIP + "'有效！")
                proxy_return = {
                    "https": str(proxy_random)
                }
                return proxy_return
            else:
                print("\033[0;44;42m返回不是代理池中的ip，代理IP无效！\033[0m")
                # 如果随机代理测试无效就从代理池中删除
                proxy_array.remove(str(proxy_random))
                PROXIES_NEW = {
                    "https": proxy_array
                }
                print(PROXIES_NEW)
                with open('./proxies_pool.json', 'w', encoding='utf-8')as f:
                    f.write(json.dumps(PROXIES_NEW))
                return None

        except Exception as e:
            print(e)
            print("\033[0;44;42m 代理IP无效！\033[0m", e)
    else:
        print("\033[0;44;42m IP代理池为空，请重新添加！\033[0m")


if __name__ == '__main__':
    proxies = get_proxy()
    print(proxies)
