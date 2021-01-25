from typing import List


class Test:

    def twoSum(self,nums:List[int],target:int)->List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

w1=Test()
print(w1.twoSum(nums=[2,7,11,15],target=9))
