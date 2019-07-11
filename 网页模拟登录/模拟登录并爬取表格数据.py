#题目连接：https://cuiqingcai.com/6829.html 

import pandas as pd
import requests, re
from pandas import DataFrame, Series, pandas

# obj = pd.Series([1,5,6,8])
# print(obj)
# print(obj.size)
# print(obj.index)
# print(obj.values)
# print('------------------------')
# obj1=pd.Series([1,5,7,9],index=['first','second','thirty','fourth'])
# print(obj1)
# print('------------------------')
# s_data={'nu':1,'li':2,'fen':3,'dou':4}
# obj2=pd.Series(s_data)
# print(obj2)
# print('------------------------')
# data={'mei':['yes','no','yes','no'],'yi':[1,2,3,4],'tian':[2.1,2.8,2.9,2.7]}
# obj3=pd.DataFrame(data)
# print(obj3)
# print(obj3.values)
# print('-----------------------')
# data1 = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002, 2003],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# # DataFrame跟Series一样，自动给数据赋index（行索引）,而列会按顺序排列好。
# frame = pd.DataFrame(data1)
# print(frame)
# # head()会返回表格的前5行数据
# print(frame.head())
url = 'https://www.ctic.org/crm?tdsourcetag=s_pctim_aiomsg'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'www.ctic.org',
}
data = {'_csrf': 'SjFKLWxVVkkaSRBYQWYYCA1TMG8iYR8ReUYcSj04Jh4EBzIdBGwmLw==',
        'CRMSearchForm[year]': '2011',
        'CRMSearchForm[format]': 'Acres',
        'CRMSearchForm[area]': 'County',
        'CRMSearchForm[region]': 'Midwest',
        'CRMSearchForm[state]': 'IL',
        'CRMSearchForm[county]': 'Adams',
        'CRMSearchForm[crop_type]': 'All',
        'summary': 'county'}
response = requests.post(url, data=data, headers=headers)
print(response.status_code)

response1 = requests.get(url, headers=headers)
html = response1.text
cookies = response1.cookies
pattern = re.compile('<meta name="csrf-token" content="(.*?)">')
csrf_token = re.findall(pattern, html)
data.update({'_crsf': csrf_token})
print(data)

response2 = requests.post(url, data=data, headers=headers, cookies=cookies)
print(response2.status_code)
