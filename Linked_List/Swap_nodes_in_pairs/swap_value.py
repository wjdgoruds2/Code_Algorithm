
class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def swapPairs(self,head:Listnode)->Listnode:
        cur=head

        while cur and cur.next:
            cur.val,cur.next.val=cur.next.val,cur.val
            cur=cur.next.next
        return head
l1=Listnode(1)
l1.next=Listnode(2)
l1.next.next=Listnode(3)
l1.next.next.next=Listnode(4)


l=Solution()
answer=l.swapPairs(l1)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next
