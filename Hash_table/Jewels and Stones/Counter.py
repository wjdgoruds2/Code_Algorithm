import collections
class Solution:
    def numJewelsInStones(self,J:str,S:str)->int:
        freqs=collections.Counter(S)  #Counter로 존재하지 않는 키는 0출력,숫자 알아서 계산
        count=0

        for char in J:
            count += freqs[char]
        return count
w=Solution()
print(w.numJewelsInStones(J="aA",S="aAAbbbb"))