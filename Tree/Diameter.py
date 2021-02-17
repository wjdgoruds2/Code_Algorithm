class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    longest:int=0
    def diameterofbinarytree(self,root:TreeNode) -> int:
        def dfs(node:TreeNode)->int:
            if not node:
                return -1
            left=dfs(node.left)
            right=dfs(node.right)

            self.longest=max(self.longest,left+right+2)   #거리
            return max(left,right) +1   #상태값
        dfs(root)
        return self.longest


l1=TreeNode(1)
l1.left=TreeNode(2)
l1.right=TreeNode(3)
l1.left.left=TreeNode(4)
l1.left.right=TreeNode(5)

w=Solution()
print(w.diameterofbinarytree(l1))
