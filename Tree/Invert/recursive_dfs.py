import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left  # 부모노드부터 스와핑
        return root




l1 = TreeNode(4)
l1.left = TreeNode(2)
l1.right = TreeNode(7)
l1.left.left = TreeNode(1)
l1.left.right = TreeNode(3)
l1.right.left = TreeNode(6)
l1.right.right = TreeNode(9)
w = Solution()
print(w.invertTree(l1))
