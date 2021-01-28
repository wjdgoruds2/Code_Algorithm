class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def swapPairs(self,head:Listnode)->Listnode:
        root=prev=Listnode(None)
        prev.next=head
        while head and head.next:
            b=head.next
            head.next=b.next
            b.next=head

            prev.next=b

            head=head.next
            prev=prev.next.next
        return root.next

l1=Listnode(1)
l1.next=Listnode(2)
l1.next.next=Listnode(3)
l1.next.next.next=Listnode(4)
l1.next.next.next.next=Listnode(5)
l1.next.next.next.next.next=Listnode(6)


l=Solution()
answer=l.swapPairs(l1)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next
