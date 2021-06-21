from operator import index
from typing import List


class Test:

    def twoSum(self,nums:List[int],target:int)->List[int]:
       for i,n in enumerate(nums):
           complement=target-n #0,2   1,7  2,11  3,15
           if complement in nums[i+1:]:
                return [nums.index(n),nums[i+1:].index(complement)+(i+1)] #nums[i+1:] 0부터 다시시작

w1=Test()
print(w1.twoSum(nums=[2,7,11,15],target=18))
