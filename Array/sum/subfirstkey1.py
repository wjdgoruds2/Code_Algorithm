from operator import index
from typing import List


class Test:

    def twoSum(self,nums:List[int],target:int)->List[int]:
        nums_map = {}
        for i, num in enumerate(nums): #키와 값을 바꿔 딕셔너리에 저장
            nums_map[num] = i  #2 0  7 1  11 2  15 3

        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return [i,nums_map[target-num]]

w1=Test()
print(w1.twoSum(nums=[2,7,11,15],target=18))
