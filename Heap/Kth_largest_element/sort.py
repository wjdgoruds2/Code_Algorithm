
from typing import List
class Solution:
    def findKthLargest(self,nums:List[int],k:int)->int:  #삽입,삭제가 없이 고정된 경우 단순정렬로 해결
        return sorted(nums,reverse=True)[k-1]
w=Solution()
print(w.findKthLargest(nums=[3,2,3,1,2,4,5,5,6],k=4))


