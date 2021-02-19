import collections
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    val:int = 0

    def bstToGst(self,root:TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root
l1 = TreeNode(4)
l1.left = TreeNode(1)
l1.right = TreeNode(6)
l1.left.left = TreeNode(0)
l1.left.right = TreeNode(2)
l1.left.right.right = TreeNode(3)
l1.right.left = TreeNode(5)
l1.right.right = TreeNode(7)
l1.right.right.right = TreeNode(8)
w = Solution()
print(w.bstToGst(l1))
