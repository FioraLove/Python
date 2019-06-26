class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        b = set(moves)
        a = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for i in b:
            a[i] = moves.count(i)
        if a['U'] == a['D'] and a['L'] == a['R']:
            return True
        else:
            return False


def main():
    pass


if __name__ == '__main__':
    print('机器人的有效动作有 R（右），L（左），U（上）和 D（下）')
    string1 = (input('请输入你的移动顺序：'))
    judge = Solution()
    judge1 = judge.judgeCircle(string1)
    print(type(judge1))
    print(judge1)
