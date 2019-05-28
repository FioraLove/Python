# 单线程爬虫
# requests获取网页源代码
# is比较的是两个整数对象的id值是否相等，也就是比较两个引用是否代表了内存中同一个地址。
# ==比较的是两个整数对象的内容是否相等，使用==时其实是调用了对象的__eq__()方法。
import dis
a=257

def main():
    b=257
    c=257
    print(b is a)
    print(a is c)
    print(b is c)
if __name__ == '__main__':
    main()

"""运行结果为：对于整数对象，Python把一些频繁使用的整数对象缓存起来，
保存到一个叫small_ints的链表中，整数对象的值定在[-5, 256]这个区间。
False
False
True
"""

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
print("the max is:",max(a,b,c))

def main(a,b):
    if a>b:
        return a
    else:
        return b
if __name__ == '__main__':
    aa = main(a,main(b,c))
    print(aa)

name = 'Hao LUO'
if name.find('L') != -1:
    print('This name has an L in it!')

chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
name = ''.join(chars)
print(name)




