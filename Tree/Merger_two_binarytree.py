class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def Mergertwobianrytree(self, t1: TreeNode,t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node=TreeNode(t1.val+t2.val)
            node.left=self.Mergertwobianrytree(t1.left,t2.left)
            node.right=self.Mergertwobianrytree(t1.right,t2.right)
            return node
        else:
            return t1 or t2



l1 = TreeNode(1)
l1.left = TreeNode(3)
l1.right = TreeNode(2)
l1.left.left = TreeNode(5)


l2 = TreeNode(2)
l2.left = TreeNode(1)
l2.right = TreeNode(3)
l2.left.right = TreeNode(4)
l2.right.right = TreeNode(7)

w = Solution()
print(w.Mergertwobianrytree(l1,l2))
