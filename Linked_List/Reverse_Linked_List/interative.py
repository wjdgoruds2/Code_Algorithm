class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: Listnode) -> Listnode:
        node,prev=head,None
        while node:
            next,node.next=node.next,prev
            prev,node=node,next
        return prev

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
