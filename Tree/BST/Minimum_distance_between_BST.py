import collections
import sys
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    prev=-sys.maxsize                               #방법1:재귀 구조 중위 순회 결과
    result=sys.maxsize
    def minDiffInBST(self,root:TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result=min(self.result,root.val-self.prev)
        self.prev=root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result



    def minDiffInBST(self,root:TreeNode) -> int:      #방법2:반복 구조 중위 순회 결과
        prev = -sys.maxsize
        result = sys.maxsize
        stack=[]
        node=root
        while stack or node:
            while node:
                stack.append(node)
                node=node.left

            node=stack.pop()

            result=min(result,node.val-prev)
            prev=node.val

            node=node.right
        return result

        return self.result



l1 = TreeNode(8)
l1.left = TreeNode(4)
l1.right = TreeNode(12)
l1.left.left = TreeNode(2)
l1.left.left.left = TreeNode(1)
l1.left.left.right = TreeNode(3)
l1.left.right = TreeNode(6)
l1.left.right.left = TreeNode(5)
l1.left.right.right= TreeNode(7)

w = Solution()
print(w.minDiffInBST(l1))
