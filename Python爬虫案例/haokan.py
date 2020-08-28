# -*- coding:utf-8 -*-
import requests
import json
import re


class Bili(object):
    def __init__(self, bv):
        self.bv = bv

    def get_url(self):
        url = self.bv
        if len(url) >= 23:
            base_url = url
        else:
            base_url = "https://m.bilibili.com/video/" + str(self.bv)
        headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }
        try:
            response = requests.get(url=base_url, headers=headers, timeout=5)
            if response.status_code == 200:
                pattern = re.compile("options = \{(.*?)\}", re.S)
                # res ="{"+ re.findall(pattern,response.text)[0]+"}"
                try:
                    res = re.findall(pattern, response.text)[0]
                    aid = re.findall("aid: (.*?),", res)[0]
                    cid = re.findall("cid: (.*?),", res)[0]
                    readyDuration = re.findall("readyDuration: (.*?),", res)[0]
                    bvid = re.findall("bvid: '(.*?)',", res)[0]
                    readyPoster = re.findall("readyPoster: '(.*?)',", res)[0]
                    readyVideoUrl = re.findall("readyVideoUrl: '(.*?)',", res)[0]
                    rows = {
                        "aid": aid,
                        "bvid": bvid,
                        "cid": cid,
                        "readyPoster": "https:" + readyPoster,
                        "readyVideoUrl": "https:" + readyVideoUrl,
                        "readyDuration": readyDuration
                    }
                    return json.dumps(rows, ensure_ascii=False)
                except Exception as e:
                    return "暂无相关数据，请检查相关数据："+str(e)
            else:
                return "暂无相关数据，请检查相关数据"
        except Exception as e:
            return e


if __name__ == '__main__':
    bili = Bili("https://haokan.baidu.com/v?vid=11231414361411904045")
    print(bili.get_url())
