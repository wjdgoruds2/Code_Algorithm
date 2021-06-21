####가장 Best방법
class Listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: Listnode) -> bool:
        rev=None
        slow=fast=head
        while fast and fast.next:                         #####홀수개는 fast.next==none이여서 if절로 but 짝수개는 fast==none이되어서 if절 안들어감
            fast=fast.next.next
            rev,rev.next,slow=slow,rev,slow.next
        if fast:                                          ####홀수개일때 중간 수 건너띄기 위함
            slow=slow.next

        while rev and rev.val==slow.val:
            slow,rev=slow.next,rev.next
        return not rev
list=Listnode(1)
list.next=Listnode(2)
list.next.next=Listnode(3)
list.next.next.next=Listnode(2)
list.next.next.next.next=Listnode(1)
list1=Solution()
print(list1.isPalindrome(list))
