JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。JSON的数据格式其实就是python里面的字典格式，里面可以包含方括号括起来的数组，也就是python里面的列表。

在python中，有专门处理json格式的模块—— json 和 picle模块
Json   模块提供了四个方法： dumps、dump、loads、load
pickle 模块也提供了四个功能：dumps、dump、loads、load
 
一. dumps 和 dump:
 dumps和dump   序列化方法
       dumps只完成了序列化为str，
       dump必须传文件描述符，将序列化的str保存到文件中
示例代码：

复制代码
>>> import json
>>> json.dumps([])    # dumps可以格式化所有的基本数据类型为字符串
'[]'
>>> json.dumps(1)    # 数字
'1'
>>> json.dumps('1')   # 字符串
'"1"'
>>> dict = {"name":"Tom", "age":23}  
>>> json.dumps(dict)     # 字典
'{"name": "Tom", "age": 23}'
复制代码
a = {"name":"Tom", "age":23}
with open("test.json", "w", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    f.write(json.dumps(a, indent=4))
    # json.dump(a,f,indent=4)   # 和上面的效果一样
保存的文件效果：



 

二. loads 和 load 

loads和load  反序列化方法

       loads 只完成了反序列化，
       load 只接收文件描述符，完成了读取文件和反序列化

实例：

>>> json.loads('{"name":"Tom", "age":23}')
{'age': 23, 'name': 'Tom'}
复制代码
import json
with open("test.json", "r", encoding='utf-8') as f:
    aa = json.loads(f.read())
    f.seek(0)
    bb = json.load(f)    # 与 json.loads(f.read())
print(aa)
print(bb)

# 输出：
{'name': 'Tom', 'age': 23}
{'name': 'Tom', 'age': 23}
