
# 练习一：继承和重写
class people:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        print("%s-%s-%s"%(self.name,self.age,self.sex))

class Student(people):
    def __init__(self,name,age,sex,salary):
        people.__init__(name,age,sex,salary)
        self.salary = salary

    def tell(self):
        print("%s是最棒的!" % self.name)


if __name__ == '__main__':

    student = Student("alex", 20, "man", 2000)
    student.tell()


# 练习二：
# class People:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def tell(self):
#         print("%s-%s-%s"%(self.name,self.age,self.sex))
#
# class Student(People):
#     def __init__(self,name,age,sex,salary):
#         # self.name = name
#         # self.age = age
#         # self.sex = sex
#         People.__init__(self,name,age,sex)
#         self.salary = salary
#
#     def tell(self):
#         print("%s是最棒的!"%self.name)
#
# if __name__ == '__main__':
#     student = Student("alex",20,"man",2000)
#     student.tell()



#练习三：
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def tell(self):
        print("%s--%s--%s"%(self.year,self.month,self.day))

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(People):
    def __init__(self,name,age,sex,year,month,day):
        People.__init__(self,name,age)
        self.sex = sex
        self.birth = Date(year,month,day)

if __name__ == '__main__':
    student = Student("alex", 25, "man", 2015, 12, 31)
    print("student的birth成员指向了一个Date对象!")
    print("%s" % student.birth)
    student.birth.tell()



# 打开本地文件
fpath = r'C:\Users\Administrator\Desktop\qq.txt'
with open(fpath,'r') as f:
    s = f.read()
    print(s)



# 创建子进程
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()  # 创建子进程，并返回进程的id，父进程返回的是父进程的id，子进程返回的是0
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))




# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):

        p.apply_async(long_time_task, args=(i,))  # 不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')




# 演示启动一个子进程并等待其结束
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process%s.'%os.getppid())
    p = Process(target=run_proc,args=('test',))  # 创建Process的实例，并传入子线程要执行的函数和参数
    print("child process will start.")
    p.start()
    p.join()  # join方法用于线程间的同步，等线程执行完毕后再往下执行
    print('child process end.')




# 使用进程池pool
from multiprocessing import Pool
import os
import time
import random


def child_task(name):
    print('子进程 %s ID是：%s 正在运行' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)  # 随机睡眠一段时间
    end = time.time()
    print('子进程 %s 运行了 %0.2f 秒' % (name, (end - start)))


if __name__ == '__main__':  # 交互模式自动开始执行
    print('当前进程(父进程)ID是：%s' % os.getpid())
    p = Pool(4)  # 创建进程池实例，大小是4个进程
    for i in range(5):  # 循环5次，每次循环都创建一个子进程，大小只有4，则第五个需要等待
        p.apply_async(child_task, args=(i,))  # apply_async方法，传入子进程要执行的函数和函数参数(以元组的形式)
    print('子进程循环创建完毕，正在等待子进程执行。。')
    p.close()  # 关闭进程池，之后就不能添加新的进程了
    p.join()  # 如果有进程池，调用join前必须调用close。（join方法，等待所有子进程执行完毕再往下执行）
    print('所有进程运行完毕')




# 进程与进程之间通过传递对象Queue来通信
from multiprocessing import Process, Queue
import os
import time
import random


def write(q):  # 写数据
    for value in ['A', 'B', 'C']:
        print('进程 %s 开始写入 %s' % (os.getpid(), value))
        q.put(value)
        time.sleep(random.random())  # 随机睡眠一段时间，开始写入第二个数据


def read(q):  # 读数据
    while True:
        value = q.get(True)
        print('进程 %s 开始读出 %s' % (os.getpid(), value))


if __name__ == '__main__':
    q = Queue()  # 父进程创建Queue，并传给各个子进程：
    pw = Process(target=write, args=(q,))  # 传入进程要执行的函数和函数参数
    pr = Process(target=read, args=(q,))

    pw.start()  # 启动子进程pw，写入:
    pr.start()  # 启动子进程pr，读取:(启动之后，就一直循环着尝试读取，直到被中断)
    pw.join()  # 等待pw结束:
    pr.terminate()  # pw进程执行结束后，就中断pr，因为pr进程里是死循环，无法等待其结束，只能强行终止:




# Python 的多线程用到的是threading模块，同启动进程类似，传入要执行的函数
import time, threading


def loop():  # 新线程要执行的函数
    print('创建了线程 %s' % threading.current_thread().name)  # current_thread()返回当前线程的名字
    for n in range(5):  # 循环五次 ， 示例代码
        print('线程 %s 循环第 %s 次' % (threading.current_thread().name, n + 1))
        time.sleep(1)  # 暂定1秒
    print('线程 %s 结束' % threading.current_thread().name)


print('最开始线程 %s 正在执行' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 传入线程要执行的函数和线程的名字，如果不指定名字，系统会有默认的线程名字
t.start()
t.join()  # 等待线程执行完毕
print('线程 %s 结束' % threading.current_thread().name)




