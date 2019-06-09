class Node(object):
    """节点"""

    def __init__(self, elem):
        # elem存放数据对象
        self.elem = elem
        self.next = None


class singleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self._head = node  # 私有属性，头结点_head

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next
        print('')

    def add(self, item):
        """链表头部添加元素，头插法"""
        node =Node(item)  #新建一个节点
        node.next=self._head  # 新节点的next指向下一节点的_head
        node._head =node  # _head指向新节点

    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)  # 定义一个新对象节点node，是一个具体的值
        if self.is_empty():
            self._head = node
        else:

            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):  # pos指明添加的位置
        """指定位置添加元素"""
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count<(pos -1):
                count +=1
                pre = pre.next
            # 当循环退出后，pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self):
        """删除节点"""
        pass
    def search(self, pos, item):
        """"""
        pass

if __name__ == '__main__':
    ll = singleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)

    print(ll.length())
    ll.travel()
