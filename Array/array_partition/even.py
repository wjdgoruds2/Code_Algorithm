from typing import List

class Test:
    def arraypairsum(self,nums:List[int])->int:
        sum=0
        nums.sort()
        for i,n in enumerate(nums):
            if i%2==0:
                sum+=n
        return sum




w1=Test()
print(w1.arraypairsum(nums=[1,4,3,2]))
