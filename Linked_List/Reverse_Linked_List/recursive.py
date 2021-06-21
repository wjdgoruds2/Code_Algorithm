class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: Listnode) -> Listnode:
       def reverse(node:Listnode,prev:Listnode=None):
           if not node:
               return prev
           next,node.next=node.next,prev
           return reverse(next,node)
       return reverse(head)

l1=Listnode(1)
l1.next=Listnode(2)
l1.next.next=Listnode(3)
l1.next.next.next=Listnode(4)
l1.next.next.next.next=Listnode(5)


l=Solution()
answer=l.reverseList(l1)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next
