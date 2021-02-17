import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self,root:TreeNode) -> int:
        if root is None:
            return 0
        queue=collections.deque([root])
        depth=0

        while queue:
            depth+=1
            for _ in range(len(queue)):
                cur_root=queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)


        return depth

l1=TreeNode(3)
l1.left=TreeNode(9)
l1.right=TreeNode(20)
l1.right.left=TreeNode(15)
l1.right.right=TreeNode(7)

w=Solution()
print(w.maxDepth(l1))
