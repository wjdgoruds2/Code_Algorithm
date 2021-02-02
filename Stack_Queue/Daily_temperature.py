from typing import List


class Solution:

    def dailyTemperature(self,T:List[int])->List[int]:
        answer=[0]*len(T) #8개를 다 0으로 리셋
        stack=[]
        for i,cur in enumerate(T):
            #현재 온도가 스택값보다 높다면
            while stack and cur >T[stack[-1]]:
                last=stack.pop()
                answer[last]=i-last
            stack.append(i)
        return answer

t=Solution()
print(t.dailyTemperature([73,74,75,71,69,72,76,73]))
