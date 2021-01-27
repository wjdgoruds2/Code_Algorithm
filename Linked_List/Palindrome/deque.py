import collections      #List 는 동적배열로 구성된 리스트여서 pop을 하면 양쪽 쉬프팅이 O(n)시간 소요됨
                        #But Deque는 이중연결리스트로 양쪽 방향추출이 O(1)시간 걸리기 때문에 deque사용이 더 시간적으로 유리하다.
from typing import Deque


class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: Listnode) -> bool:
        q: Deque=collections.deque()

        if not head:
            return True
        node=head
        while node is not None:
            q.append(node.val)
            node=node.next
        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        return True
list=Listnode(1)
list.next=Listnode(2)
list.next.next=Listnode(3)
list.next.next.next=Listnode(2)
list.next.next.next.next=Listnode(1)
list1=Solution()
print(list1.isPalindrome(list))
