class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def oddEvenList(self,head:Listnode)->Listnode:
        if head is None:
            return None
        odd=head
        even=head.next
        even_head=head.next  #마지막에 홀수노드에서 연결할 짝수노드 젤 앞

        while even and even.next:
            odd.next,even.next=odd.next.next,even.next.next
            odd,even=odd.next,even.next

        odd.next=even_head
        return head
l1=Listnode(1)
l1.next=Listnode(2)
l1.next.next=Listnode(3)
l1.next.next.next=Listnode(4)
l1.next.next.next.next=Listnode(5)
l1.next.next.next.next.next=Listnode(6)


l=Solution()
answer=l.oddEvenList(l1)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next
