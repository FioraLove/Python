# 实现树结构的类，树的节点有三个私有属性  左指针 右指针 自己的值
class Node():

    def __init__(self, data=None, left=None, right=None):  # data代表根节点，left代表左节点，right代表右节点
        self._data = data
        self._left = left
        self._right = right


# 先序遍历  遍历过程 根左右
def pro_order(tree):
    if tree == None:
        return False
    print(tree._data, end=' ')
    pro_order(tree._left)
    pro_order(tree._right)


# 后序遍历 遍历过程：左 右 根
def pos_order(tree):
    if tree == None:
        return False
    # print(tree.get_data())
    pos_order(tree._left)
    pos_order(tree._right)
    print(tree._data, end=' ')


# 中序遍历 遍历过程： 左 根 右
def mid_order(tree):
    if tree == None:
        return False
    # print(tree.get_data())
    mid_order(tree._left)
    print(tree._data, end=' ')
    mid_order(tree._right)


# 层次遍历 遍历过程：从上至下，从左至右
def row_order(tree):
    # print(tree._data)
    queue = []
    queue.append(tree)
    while True:
        if queue == []:
            break
        print(queue[0]._data, end=' ')
        first_tree = queue[0]
        if first_tree._left != None:
            queue.append(first_tree._left)
        if first_tree._right != None:
            queue.append(first_tree._right)
        queue.remove(first_tree)


if __name__ == '__main__':
    tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))  # 注意描述一棵树的节点的规范
    print('-------先序遍历---------')
    pro_order(tree)

    print('\n\n-------中序遍历---------')
    mid_order(tree)
    print('\n\n-------后序遍历---------')
    pos_order(tree)
    print('\n\n--------层次遍历--------')
    row_order(tree)
