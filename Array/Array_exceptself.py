from typing import List

class Test:
    def productExceptSelf(self,nums:List[int])->List[int]:
        out=[]
        p=1
        for i in range(0,len(nums)): #i를 기준으로 왼쪽 곱
            out.append(p)
            p=p*nums[i]
        p=1
        for i in range(len(nums)-1,0-1,-1):#i를 기준으로 오른쪽 곱
            out[i]=out[i]*p
            p=p*nums[i]

        return out



w1=Test()
print(w1.productExceptSelf(nums=[1,4,3,2]))
