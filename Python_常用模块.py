from datetime import datetime
mytime = datetime(2019,5,31,3,4,5)
print(mytime)

mytime1 = datetime.strptime('2015-12-11 18:22:33', '%Y-%m-%d %H:%M:%S')  # 第二个参数是时间格式
print (mytime1)



# datetime转换成字符串
now = datetime.now()
print (now.strftime('%a, %b %d %H:%M'))

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print (p.x, p.y)


# 双向列表deque
from collections import deque

L = ['A', 'B', 'C']
dq = deque(L)  # dq即为一个双向列表
dq.append('D')  # 在末尾添加-----还有pop和popleft，用法同list
dq.appendleft('XXX')  # 在开始处添加
print (L)  # 原始L的列表不变
print (dq)
print (dq[0])  # 可下标访问


