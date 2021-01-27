####가장 Best방법
class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: Listnode, l2: Listnode) -> Listnode:
        if (not l1) or (l2 and l1.val > l2.val):  #not l1 ==맨 마지막 l1.next==none일때 사용
            l1,l2=l2,l1
        if l1:
            l1.next=self.mergeTwoLists(l1.next,l2) #########마지막에는 둘다 None이됨
        return l1

l1=Listnode(1)
l1.next=Listnode(2)
l1.next.next=Listnode(4)

l2=Listnode(1)
l2.next=Listnode(3)
l2.next.next=Listnode(4)

l=Solution()
answer=l.mergeTwoLists(l1,l2)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next
