import re


class iscell(object):
    def __init__(self):
        self.p = re.compile('^((13[0-9])|(15[^4,\\D])|(18[0,5-9]))\\d{8}|(^[1]([3][0-9]{1}|59|58|88|89)[0-9]{8})$')

    def iscellphone(self, number):
        res = self.p.match(number)
        if res:
            return True
        else:
            return False


p = iscell()
f = open("user_info.txt", "r")
data = f.read()
contacts = re.findall("[0-9]{11}", data)
for i in contacts:
    if p.iscellphone(i):
        print("%s 是正常号码" % i)
    else:
        print("请检查手机号码%s" % i)
