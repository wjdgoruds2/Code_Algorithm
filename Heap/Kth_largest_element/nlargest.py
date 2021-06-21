import heapq
from typing import List
class Solution:
    def findKthLargest(self,nums:List[int],k:int)->int:
        return heapq.nlargest(k,nums)[-1]   #k번째만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴한다.
w=Solution()
print(w.findKthLargest(nums=[3,2,3,1,2,4,5,5,6],k=4))


