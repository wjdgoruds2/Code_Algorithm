from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:   #q에  1 2 3 2 1
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1: # 1 1    2 2
            if q.pop(0) != q.pop():
                return False

        return True
list=ListNode(1)
list.next=ListNode(2)
list.next.next=ListNode(3)
list.next.next.next=ListNode(2)
list.next.next.next.next=ListNode(1)
list1=Solution()
print(list1.isPalindrome(list))
