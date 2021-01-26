from typing import List


class Test:
    def arraypairsum(self,nums:List[int])->int:
        sum=0
        pair=[]
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair)==2:
                sum+=min(pair)
                pair=[]

        return sum




w1=Test()
print(w1.arraypairsum(nums=[1,4,3,2]))
