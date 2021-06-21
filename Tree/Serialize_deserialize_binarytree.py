######python은 pickle이라는 직렬화 모듈을 기본으로 제공한다. 직렬화 알고리즘 제약 없어서 bfs dfs상관없음  bfs가 보기 더편하긴함
# 부모:i/2 자신:i 왼쪽 자식:2i 오른쪽 자식:2i+1
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result=['#']

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ''.join(result)
    def deserialize(self, data: str) -> TreeNode:
        if data['# #']:
            return None

        nodes=data.split()

        root=TreeNode(int(nodes[1]))
        queue=collections.deque([root])
        index=2
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left=TreeNode(int(nodes[index]))
                queue.append(node.left)
            index+=1
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root

l1 = TreeNode(1)
l1.left = TreeNode(2)
l1.right = TreeNode(3)
l1.right.left = TreeNode(4)
l1.right.right = TreeNode(5)


w = Solution()
print(w.serialize(l1))
