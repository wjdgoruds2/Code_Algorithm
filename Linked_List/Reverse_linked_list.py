class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseBetween(self,head:Listnode,m:int,n:int)->Listnode:
        if not head or m==n:
            return head
        root=start=Listnode(None)
        root.next=head
        for _ in range(m-1):
            start=start.next
        end=start.next

        for _ in range(n-m):
            tmp,start.next,end.next=start.next,end.next,end.next.next
            start.next.next=tmp
l1=Listnode(1)
l1.next=Listnode(2)
l1.next.next=Listnode(3)
l1.next.next.next=Listnode(4)
l1.next.next.next.next=Listnode(5)
l1.next.next.next.next.next=Listnode(6)


l=Solution()
answer=l.reverseBetween(l1,m=2,n=4)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next
