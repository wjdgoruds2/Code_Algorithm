import collections
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMinHeightTrees(self, n:int, edges:List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph=collections.defaultdict(list)
        #양방향 그래프
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        #첫번쨰 리프 노드 추가
        leaves=[]
        for i in range(n+1):
            if len(graph[i])==1:
                leaves.append(i)

        while n>2:
            n-=len(leaves)
            new_leaves=[]
            for leaf in leaves:
                neighbor=graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor])==1:
                    new_leaves.append(neighbor)

            leaves=new_leaves
        return leaves


l1 = TreeNode(4)
l1.left = TreeNode(2)
l1.right = TreeNode(7)
l1.left.left = TreeNode(1)
l1.left.right = TreeNode(3)
l1.right.left = TreeNode(6)
l1.right.right = TreeNode(9)
w = Solution()
print(w.findMinHeightTrees(n=10,edges=[[1,3],[2,3],[3,4],[3,5],[4,6],[6,10],[5,7],[5,8],[8,9]]))
