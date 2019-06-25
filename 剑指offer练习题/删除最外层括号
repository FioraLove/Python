"""
遍历字符串，用栈存，左括号入，右括号出，
当栈长度为零，即找到一个，去掉头尾字符，将所有处理过的拼接起来，即最终答案
"""
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 定义一个空栈
        stack = []
        # 定义一个空字符串，用于保存结果
        result = ''
        # i用来表示字符串每一个数的索引
        i = 0
        # 当不为空时，一直执行程序
        while len(S) != 0:
            # 当遇到左括号时，用栈保存
            if S[i] == '(':
                stack.append('(')
            # 当遇到右括号时，出栈
            else:
                stack.pop()
            i += 1
            if len(stack) == 0:
                # 去掉首尾字符
                result += S[1:i - 1]
                S = S[i:]
                i = 0
        return result


delelt = Solution()
print(delelt.removeOuterParentheses("(()())(())"))
