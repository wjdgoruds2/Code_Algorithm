from typing import List


class Test:

    def threeSum(self,nums:List[int])->List[List[int]]:
        results=[]
        nums.sort()

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right= i+1,len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    results.append((nums[i],nums[left],nums[right]))

                    while left<right and nums[left]==nums[left+1]: #ex)2 -1 -1 0 -1  뒤에 중복된것이 나오면  -1 0 -1 의 경우가 또 나올 수 있어서 중복 제거
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1

        return results




w1=Test()
print(w1.threeSum(nums=[-1,0,1,2,-1,-4]))
