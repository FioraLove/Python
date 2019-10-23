import re
import requests
import pygal


# url = 'https://pubgm.qq.com/zlkdatasys/a20171229jdcs/akm.shtml'
class Game(object):
    # 用于下载和绘制吃鸡游戏的雷达图
    def __init__(self):
        # 获取枪类的主网页的url
        self.url = 'https://pubgm.qq.com/zlkdatasys/a20171229jdcs/list.shtml'
        # 发送请求，获取回应
        self.response = requests.get(self.url)
        # 返回网页内容，以gbk编码，否则会乱码
        html = self.response.content.decode('gbk')
        """获取每一把枪的地址"""
        # 利用正则，筛选网页的所有枪类的url
        self.res = re.compile(r'<a href="(.*?)" target="_blank" class="btn_xq datum_list_sp"')  # 此刻不能加re.S，否则会出现很多无关数据
        self.res2 = re.findall(self.res, html)
        # 找到每一把枪的名称
        self.name = re.findall(r'<div class="qx_tab_name">(.*?)</div>', html)
        # 只选择步枪类的名字，前七个均是步枪
        self.name = self.name[1:8]

    """绘制雷达图"""

    def plotGame(self):
        # 用于绘图
        # data用于保存每一把枪的性能数据
        data = []
        num = 0

        # 枪的性能
        for ii in self.res2:
            if num < 7:
                num += 1
                ii = "https://pubgm.qq.com" + ii

                a = requests.get(ii).text
                self.res1 = re.compile(r'<span style="width:(.*?)%;"></span>')
                self.reg1 = re.findall(self.res1, a)
                data.append([int(self.reg1[0]), int(self.reg1[1]), int(self.reg1[2]), int(self.reg1[3])])

        # 调用Rader类，并设置雷达图的填充（fill=True），及数据范围（range（0,100））
        radar_chart = pygal.Radar()
        radar_chart.title = '步枪性能'
        radar_chart.x_labels = ['射速', '威力', '射程', '稳点']

        for ff, property in zip(self.name, data):
            print(ff, property)
            # 绘制雷达图区域
            radar_chart.add(ff, property)
        # 保存图像
        radar_chart.render_to_file('步枪性能图.svg')


if __name__ == '__main__':
    game = Game()
    game.plotGame()
