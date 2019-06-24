class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int):
        if not root:
            return
        if root.val==val:
            return root
        elif root.val>val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
if __name__ == '__main__':
    a = Node(15)
    b = Node(6)
    c = Node(18)
    d = Node(4)
    e = Node(8)
    f = Node(17)
    g = Node(20)
    h = Node(13)
    i = Node(9)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.right = h
    h.left = i
    ff = Solution()
    ff1=ff.searchBST(b,20)
    print(ff1)
