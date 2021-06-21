class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
   def invertTree(self, root:TreeNode)-> TreeNode:
       if root:
           root.left,root.right= \
            self.invertTree(root.right),self.invertTree(root.left)
           return root
       return None

l1=TreeNode(4)
l1.left=TreeNode(2)
l1.right=TreeNode(7)
l1.left.left=TreeNode(1)
l1.left.right=TreeNode(3)
l1.right.left=TreeNode(6)
l1.right.right=TreeNode(9)
w=Solution()
print(w.invertTree(l1))
