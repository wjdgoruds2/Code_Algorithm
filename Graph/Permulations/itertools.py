import itertools ###itertools -> 효율적인 루핑을 위한 이터레이터를 만드는 함수
from typing import List

class Solution:
    def permute(self,nums:List[int])->List[List[int]]:
        return list(itertools.permutations(nums))  #nums의 모든 가능한 순서,반복되는 요소 없음
#(itertools)모음
#product(,repeat=숫자)->반복이 있는 요소
#permutations(,숫자)->반복이 없는 요소
#combinations(,숫자)->정렬 + 반복이 없는 요소
#combinations_with_replacement(,숫자)->정렬+ 반복이 있는 요소
w=Solution()
print(w.permute(nums=[1,2,3]))
