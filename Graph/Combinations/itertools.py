from typing import List
import itertools
class Solution:
    def combine(self,n:int,k:int)->List[List[int]]:
        return list(itertools.combinations(range(1,n+1),k))
w=Solution()
print(w.combine(n=4,k=2))
