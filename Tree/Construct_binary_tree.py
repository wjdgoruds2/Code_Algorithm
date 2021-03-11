from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self,preorder:List[int],inorder:List[int])->TreeNode:
        if inorder:
            index=inorder.index(preorder.pop(0))
            node=TreeNode(inorder[index])
            node.left=self.buildTree(preorder,inorder[0:index])
            node.right=self.buildTree(preorder,inorder[index+1:])

            return node
w=Solution()
print(w.buildTree(preorder=[1,2,4,5,3,6,7,9,8],inorder=[4,2,5,1,7,9,6,8,3]))
