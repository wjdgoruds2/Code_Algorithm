class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result:int=0
    def longestUnivaluePath(self,root:TreeNode) -> int:
        def dfs(node:TreeNode)->int:
            if not node:
               return 0
            left=dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left+=1
            else:
                left=0
            if node.right and node.right.val == node.val:
                right+=1
            else:
                right=0

            self.result=max(self.result,right+left)
            return max(left,right)

        dfs(root)
        return self.result




l1=TreeNode(1)
l1.left=TreeNode(1)
l1.right=TreeNode(1)
l1.left.left=TreeNode(1)
l1.left.right=TreeNode(2)
l1.right.right=TreeNode(3)
w=Solution()
print(w.longestUnivaluePath(l1))
