from typing import List


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
    def toList(self,node:Listnode)->List:
        list:List=[]
        while node:
            list.append(node.val)
            node=node.next
        return list
    def toReverseLinkedList(self,result:str)->Listnode:
        prev:Listnode=None
        for r in result:
            node=Listnode(r)
            node.next=prev
            prev=node
        return node

    def addTwoNumbers(self,l1:Listnode,l2:Listnode)->Listnode:
        a=self.toList(self.reverseList(l1))
        b=self.toList(self.reverseList(l2))

        reultStr=int(''.join(str(e) for e in a))+\
                 int(''.join(str(e) for e in b))

        return self.toReverseLinkedList(str(reultStr))

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
