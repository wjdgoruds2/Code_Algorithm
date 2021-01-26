from typing import List

class Test:
    def arraypairsum(self,nums:List[int])->int:
       return sum(sorted(nums)[::2])#########슬라이싱 사용




w1=Test()
print(w1.arraypairsum(nums=[1,4,3,2]))
