class TreeNode(object):
    def __init__(self,val ,left =None,right =None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    if not root:
        return 0
    result = 0
    if L <= root.val <= R:
        result += root.val
    if L <= root.val:  # 如果当前节点比左边界小，则该节点的左子树不用遍历了（都是小于该节点的值，已超出范围）
        result += self.rangeSumBST(root.left, L, R)
    if root.val <= R:  # 如果当前节点比右边界大，则该节点的右子树不用遍历了（都是大于该节点的值）
        result += self.rangeSumBST(root.right, L, R)
    return result
def main(tree):
    # a = TreeNode(15)
    # b = TreeNode(6)
    # c = TreeNode(18)
    # d = TreeNode(4)
    # e = TreeNode(8)
    # f = TreeNode(17)
    # g = TreeNode(20)
    #
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.left = f
    # c.right = g

    #ff = Solution()
    tree =TreeNode(10, TreeNode(5, 3,7), TreeNode(15, 13,18))
    #ff1 = rangeSumBST(tree,7,13)



if __name__ == '__main__':
    tree = TreeNode(10, TreeNode(5, 3, 7), TreeNode(15, 13, 18))
    print(rangeSumBST(tree,7,13))
