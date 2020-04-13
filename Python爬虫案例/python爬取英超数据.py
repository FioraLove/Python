"""
目标url:url = "https://www.msn.cn/zh-cn/sports/soccer/chinese-super-league/standings/sp-s-r-a-true"
"""

import requests
import time
import json
from pyquery import PyQuery as pq

url = "https://www.msn.cn/zh-cn/sports/soccer/chinese-super-league/standings/sp-s-r-a-true"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "referer": "https://www.msn.cn/zh-cn/sports/soccer/chinese-super-league/standings"
}

try:
    response = requests.get(url=url, headers=headers, timeout=10)
    if response.status_code == 200:
        doc = pq(response.text)
        thead = doc("#standings table thead tr th a")
        for i in thead.items():
            print(i.text(), end=" ")
        print("")

        # 获取表格具体数据
        html = doc("#standings table tbody tr")
        for i in html.items():
            rank = i.find("td").eq(0).text()
            img = json.loads(i.find("td").eq(1)("img").attr("data-src"))["default"]
            teamname = i.find("td").eq(2).text()
            times = i.find("td").eq(3).text()
            shengchang = i.find("td").eq(4).text()
            pingju = i.find("td").eq(5).text()
            fu = i.find("td").eq(6).text()
            score = i.find("td").eq(10).text()
            print(
                rank + "  " + "https:" + img + " " + teamname + " " + times + " " +
                shengchang + " " + pingju + " " + fu + " " + score + "\n")
            time.sleep(2)
except Exception as e:
    print(e)
