from flask import Flask
# 导入这个库，新建一个名为“templates”的directory。只能命名为templates
from flask import render_template
from flask import request
app = Flask(__name__)


# 路由
@app.route('/')  # 加一个'/'代表当前网站 # 装饰器：给函数增加功能
def idex():
    return render_template('HTML2.html')


@app.route('/s')  # 指传到另一个界面上
def load():
    return render_template('HTML3.html')


@app.route('/m')
def cg():
    name=request.args.get("name")
    sex=request.args.get("sex")
    age=request.args.get("age")
    Tel=request.args.get("Tel")
    print('你的签到情况：')
    print('姓名：%s  年纪：%s  性别：%s  电话：%s'%(name,age,sex,Tel))
    return render_template('HTML4.html')


app.run()
