import heapq
from typing import List
import collections

class Solution:
    def topKFrequent(self,num:List[int],k:int)->List[int]:
        freqs=collections.Counter(num)
        freqs_heap=[]
        for f in freqs:
            heapq.heappush(freqs_heap,(-freqs[f],f)) #######힙은 최소힙만 제공 + 빈도수를 중심으로 나열하기 위해 순서 바꿈
        top=list()

        for _ in range(k):
            top.append(heapq.heappop(freqs_heap)[1])
        return top

w=Solution()
print(w.topKFrequent(num=[1,1,1,2,2,3],k=2))
