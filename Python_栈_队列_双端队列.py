# """
# Stack（）创建一个空栈
# """
# class Stack(object):
#     def __init__(self):
#         # 列表和字典都可以视为栈，以列表为作为开栈口
#         # 因为在表尾添加或删除元素的时间复杂度为O(1)
#         self._list =[]
#
#     def push(self,item):
#         # 添加一个元素item到栈顶
#         self._list.append(item)
#
#     def pop(self):
#         # 弹出栈顶元素
#         return self._list.pop()
#
#     def peek(self):
#         # 返回一个栈顶元素
#         if self._list:
#             return self._list[-1]
#         else:
#             return None
#
#     def is_empty(self):
#         # 判断栈是否为空
#         return self._list == []
#
#     def size(self):
#         # 返回栈的元素个数
#         return len(self._list)
#
#
# if __name__ == '__main__':
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     print(s.size())
#     print(s.pop())
#     print(s.pop())
#     print(s.size())
#     print(s.is_empty())
#
#
# class Queue(object):
#     # 队列（先进先出）
#     def __init__(self):
#         self._list = []  # 初始化构造函数，空的列表私有化保存元素
#
#     def enqueue(self, item):
#         # 往队列中增加一个item元素
#         self._list.append(item)
#
#     def dequeue(self):
#         # 列表头部删除一个元素
#         return self._list.pop(0)
#
#     def is_empty(self):
#         # 判断一个队列是否为空
#         return self._list == []
#
#     def size(self):
#         # 返回队列的大小
#         return len(self._list)
#
#
# if __name__ == '__main__':
#     s = Queue()
#     s.enqueue(1)
#     s.enqueue(2)
#     print(s.size())
#     print(s.dequeue())
#     print(s.dequeue())
#     print(s.size())
#     print(s.is_empty())


# class Deque(object):
#     # 队列（先进先出）
#     def __init__(self):
#         self._list = []  # 初始化构造函数，空的列表私有化保存元素
# 
#     def add_front(self, item):
#         # 往队列中增加一个item元素
#         self._list.insert(0, item)
# 
#     def add_rear(self, item):
#         # 往队列尾部添加一个元素
#         self._list.insert(item)
# 
#     def pop_front(self):
#         # 从队列头部删除一个元素
#         return self._list.pop(0)
# 
#     def pop_rear(self):
#         # 从一个队列尾部删除一个元素
#         return self._list.pop()
# 
#     def is_empty(self):
#         # 判断一个队列是否为空
#         return self._list == []
# 
#     def size(self):
#         # 返回队列的大小
#         return len(self._list)
# 
# 
# if __name__ == '__main__':
#     s = Deque()
