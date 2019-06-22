'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''


# 实现一个链表类，只有一个值val和一个指向下一个节点的next'指针'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # @listNode: 头结点
        # write code here
        l = []
        if listNode is None:
            l.next = b
            return l.next

            b.next = c
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]


# 创建链表 a->b->c
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

# 实例化
demo = Solution()
print(demo.printListFromTailToHead(a))
