"""
reduce() 函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果
"""
from functools import reduce
s='www.baidu.com'
result = reduce(lambda x,y:y+x,s)
print(result)

# 冒号:之前的a,b,c表示它们是这个函数的参数。
# 匿名函数不需要return来返回值，表达式本身结果就是返回值。
