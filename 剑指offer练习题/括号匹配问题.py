# -*- coding:UTF-8 -*-
def kuohao_match(exp):
    # 以列表为栈
    stack = []
    # 目标条件匹配
    items = {'(': ')', '{': '}', '[': ']'}
    # 遍历目标字符串
    for item in exp:
        # 遍历item是否含有这三种字符
        if item in {'(', '{', '['}:
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            # 返回栈顶元素,pop() 函数用于移除列表中的一个元素(默认最后一个元素)
            top = stack.pop()
            if items[top] != item:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


print(kuohao_match('()[]{([]][]}()'))
