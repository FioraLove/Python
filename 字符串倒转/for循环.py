"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。索引从0开始。
"""

def func(s):
    result = ""
    max_index = len(s)-1
    for index,value in enumerate(s):
        result += s[max_index-index]
    return result
result = func(s)
