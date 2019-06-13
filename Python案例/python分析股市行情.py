import json,pygal,math
import requests

json_url ='http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sz000001&scale=5&ma=5&datalen=1023'
response = requests.get(json_url)

with open('gs.json','w') as f:
    f.write(json.dumps(response,ensure_ascii=False)+'\n')
file_re= response.json()
print(file_re)

# 将数据加载到一个列表中
file_name='gs.json'
with open(file_name) as f:
    gs_data=json.load()

# 创建列表，分别储存日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
closes = []

#打印每一天的信息
for gs_data in gs_data:
    dates.append(gs_data['date'])  # 把时间信息存储在新的空列表，成了单一列表
    months.append(gs_data['month'])
    weeks.append(gs_data['weeks'])
    weekdays.append(gs_data['weekday'])
    closes.append(int(float(gs_data['close'])))
view = pygal.line(x_label_rotation=20,show_minor_x_labels=False)

view.title = ('收盘价（￥）')
view.x_labels =dates
closes_log = [math.log(i) for i in closes]  # 收盘价对数变换
view.add('收盘价',closes_log)
view.render_in_browser()


#分组展示收盘价平均值
def day(x_data,y_data,title,y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda i:i[0]):# sorted()匿名
        #将x轴与y轴的数据合并，排序，分组
        xy_map.append([x,sum(y_list)] /len(y_list)])  #每一分组的平均值
        x_unique,y_mean=[]
