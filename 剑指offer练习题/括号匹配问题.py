# -*- coding:UTF-8 -*-
def kuohao_match(exp):
    stack = []
    di = {'(': ')', '{': '}', '[': ']'}
    for c in exp:
        if c in {'(', '{', '['}:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if di[top] != c:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


print(kuohao_match('()[]{([]][]}()'))
