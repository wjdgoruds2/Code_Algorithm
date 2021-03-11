import heapq
from typing import List
class Solution:
    def findKthLargest(self,nums:List[int],k:int)->int:
        heapq.heapify(nums)  #자료구조가 힙 특성에 맞도록 바꿔주는 연산으로 추가가 발생하지 않는다면 적당

        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
w=Solution()
print(w.findKthLargest(nums=[3,2,3,1,2,4,5,5,6],k=4))


