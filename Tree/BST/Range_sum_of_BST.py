import collections
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self,root:TreeNode,L:int,R:int) -> TreeNode:   #방법1:재귀
        if not root:
            return 0
        return(root.val if L <=root.val <=R else 0)+self.rangeSumBST(root.left,L,R)+self.rangeSumBST(root.right,L,R)


    def rangeSumBST(self,root:TreeNode,L:int,R:int) -> TreeNode:   #방법2:DFS
        def dfs(node:TreeNode):
            if not node:
                return 0
            if node.val < L:
                return dfs(node.right)
            elif node.val >R:
                return dfs(node.left)
            return node.val+dfs(node.left)+dfs(node.right)
        return dfs(root)

    def rangeSumBST(self,root:TreeNode,L:int,R:int) -> TreeNode:   #방법3:반복구조 DFS
        stack,sum=[root],0
        while stack:
            node=stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val <R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum+=node.val

        return sum



    def rangeSumBST(self,root:TreeNode,L:int,R:int) -> TreeNode:   #방법4:반복구조 BFS
        stack, sum = [root], 0
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val

        return sum


l1 = TreeNode(10)
l1.left = TreeNode(5)
l1.right = TreeNode(15)
l1.left.left = TreeNode(3)
l1.left.right = TreeNode(7)
l1.right.right = TreeNode(18)

w = Solution()
print(w.rangeSumBST(root=l1,L=7,R=15))
