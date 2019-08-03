"""
装饰器decorator：本质上是一个函数，用于装饰其它函数（为其它函数添加附加功能）
原则：不能修改被装饰的函数的源代码；不能修改被装饰的函数的调用方式。
函数名即为内存地址，类似于一个门牌号，比如fun（）函数，print（fun）即打印其内存地址
装饰器常常用于对已发布的程序功能，进行添加功能
"""
import time

def test1():
    start  = time.time()
    time.sleep(3)
    end = time.time()
    print('hello python')
    print('%d'%(end-start))

test1()

"""
lambda:匿名函数，即函数名不存在，涉及到Python内存回收机制
"""
def fun(func):
    func()
    print(func)
fun(test1)

"""
装饰器=嵌套函数+高阶函数
"""
装饰器实例
import time


def timer(func):  # 装饰器timer
    def decorator():  # 装饰函数 =高阶函数+嵌套函数
        start_time = time.time()
        func()  # 注意点
        end_time = time.time()
        print('the process cost:%s second' % (end_time - start_time))

    return decorator


@timer
def test1():
    time.sleep(3)
    print('hello java')


@timer
def test2():
    time.sleep(3)
    print('hello python')
    
test2()
test1()  # 此时不能加括号，加括号后会返回被装饰函数的值

"""
带非固定参数：
import time

def timer(func):  #装饰器timer
    def decorator(*args,**kwargs):  #装饰函数 =高阶函数+嵌套函数
        start_time = time.time()
        func(*args,**kwargs)  # 注意点，这里表示被装饰的函数所执行的内容
        end_time = time.time()
        print('the process cost:%s second'%(end_time-start_time))
    return decorator  # 注意点

@timer
def test1(name,age):
    time.sleep(3)
    print('test1:',name,age)
    print('hello java')

test1('alex',21)
"""

