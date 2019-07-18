import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,STOPWORDS
# 导入科学计算模块
import numpy as np
# 导入图片处理模块
from PIL import Image

with open(r'./word.txt','r',encoding='utf-8',errors='ignore') as f:
     info = f.read()

# 分词
infocut = jieba.cut(info,cut_all=True)
# 把生成器join成字符串
info = ''.join(infocut)
print(info)

bgcolor = np.array(Image.open('./5b70fd1f32a6b.jpg'))
# print(bgcolor)
stopwords = set(STOPWORDS)
stopwords.add("said")
myWordCloud = WordCloud(font_path='simkai.ttf',  # 中文字体库
                         #width=1200, height=800,  # 宽，高
                         mask=bgcolor,  # 字体颜色
                         scale=1,  # 缩放
                         max_words=200,  # 最大字数
                         min_font_size=4,  # 最小字体大小
                         stopwords=stopwords,  # 终止词
                         random_state=90,  # 随机状态，单位°
                         background_color='white',  # 背景颜色
                         max_font_size=200,  # 最大字体大小
                         ).generate(info)  # 生成词云

# 绘制词云，带坐标
# plt.imshow(myWordCloud)
# plt.show()

# 绘制词云，不带坐标

plt.figimage(myWordCloud)
# plt.show()

# 保存
plt.savefig('python岗位.png')
