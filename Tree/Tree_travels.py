class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode('F', TreeNode('B', TreeNode('A'), TreeNode('D', TreeNode('C'), TreeNode('E'))),
                TreeNode('G', None, TreeNode('I', TreeNode('H'))))
class Solution:
    def preorder(self,node):
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)

w=Solution()
print("//////////전위/////////")
w.preorder(root)
print("//////////중위/////////")
w.inorder(root)
print("//////////후위/////////")
w.postorder(root)