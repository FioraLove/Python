题目1:
l1=[1,2,3]
l2=[4,5]
求： calculate(l1)+calculate(l2) ＝ 168
其中，各个数组很大，无法直接加载到内存中

解：
'''
迭代使用的是循环结构。
递归使用的是选择结构。
'''

# 递归求解
def calculate(l):
    if len(l) <= 1:
        return l[0]
    value = calculate(l[1:])
    return 10**(len(l) - 1) * l[0] + value


# 迭代求解
def calculate2(l):
    result = 0
    while len(l) >= 1:
        result += 10 ** (len(l)-1) * l[0]
        l = l[1:]
    return result


l1 = [1, 2, 3]
l2 = [4, 5]
sum = 0
result = calculate(l1) + calculate(l2)
result2 = calculate2(l1) + calculate2(l2)
print(result)
print(result2)
