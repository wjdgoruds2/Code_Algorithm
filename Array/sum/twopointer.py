
from typing import List #############투포인터를 사용하면 인덱스 값이 망가져 인덱스값을 구할 수 는 없지만 만약 값만 찾는다면 좋은 방법


class Test:

    def twoSum(self,nums:List[int],target:int)->List[int]:
        nums.sort()
        left,right=0,len(nums)-1
        while not left==right:
            if nums[left]+nums[right]<target:
                left+=1
            elif nums[left]+nums[right]>target:
                right-=1
            else:
                return [left,right]

w1=Test()
print(w1.twoSum(nums=[2,7,11,15],target=18))
