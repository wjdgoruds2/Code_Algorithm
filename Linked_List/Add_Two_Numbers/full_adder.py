#이진법이 아니라 삼진법:입력값 A,B 자리올림수 Carry
from typing import List


class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self,l1:Listnode,l2:Listnode)->Listnode:
        root=head=Listnode(0)
        carry=0
        while l1 or l2 or carry:
            sum=0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next

            carry,val=divmod(sum+carry,10)
            head.next=Listnode(val)
            head=head.next
        return root.next
l1=Listnode(2)
l1.next=Listnode(4)
l1.next.next=Listnode(3)

l2=Listnode(5)
l2.next=Listnode(6)
l2.next.next=Listnode(4)


l=Solution()
answer=l.addTwoNumbers(l1,l2)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next
