s='www.baidu.com'
def func(s):
    if len(s) <1:
        return s
    return func(s[1:])+s[0]
result = func(s)
