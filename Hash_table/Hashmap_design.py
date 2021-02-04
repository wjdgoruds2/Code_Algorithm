#########python은 원래 오픈 어드레싱 방법
#########But 이건 개별 체이닝 방법(:연결리스트)으로 구현
import collections
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class MyHashMap:
    def __init__(self):
        self.size=1000
        self.table=collections.defaultdict(ListNode)
    def put(self,key:int ,value:int)->None:
        index= key % self.size
        if self.table[index].value is None:
            self.table[index]=ListNode(key,value)
            return
        p=self.table[index]
        #해당 인덱스에 값이 존재한다면 연결리스트로 처리
        while p:
            if p.key ==key:
                p.value=value
                return
            if p.next is None:
                break
            p=p.next
        p.next=ListNode(key,value)

    def get(self,key:int)->int:
        index=key % self.size
        if self.tabel[index].value is None:
            return -1
        p=self.table[index]
        while p:
            if p.key ==key:
                return p.value
            p=p.next
        return -1

    def remove(self,key:int)->None:
        index=key % self.size
        if self.table[index].value is None:
            return
        p=self.table[index]
        if p.key ==key:
            self.table[index]=ListNode() if p.next is None else p.next
            return
        prev=p
        while p:
            if p.key == key:
                prev.next=p.next
                return
            prev,p=p,next

