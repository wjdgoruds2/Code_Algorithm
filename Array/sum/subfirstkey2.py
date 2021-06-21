
from typing import List


class Test:

    def twoSum(self,nums:List[int],target:int)->List[int]:
        nums_map = {}
        for i, num in enumerate(nums): #키와 값을 바꿔 딕셔너리에 저장
            if target-num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num]=i

w1=Test()
print(w1.twoSum(nums=[2,7,11,15],target=18))
