#이진균형트리는 왼쪽 오른쪽 높이 차이가 1이하인것 !

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0

            left=check(root.left)
            right=check(root.right)

            if left == -1 or right == -1 or abs(left-right)>1:
                return -1  #높이 차이가 2이상이면 최종 부모노드를 -1로 리턴
            return max(left,right)+1
        return check(root) != -1 #부모노드가 -1이면 false return

l1 = TreeNode(3)
l1.left = TreeNode(9)
l1.right = TreeNode(20)
l1.right.left = TreeNode(15)
l1.right.right = TreeNode(7)

w = Solution()
print(w.invertTree(l1))
