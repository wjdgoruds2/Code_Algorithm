import collections
class Solution:
    def numJewelsInStones(self,J:str,S:str)->int:
        freqs=collections.defaultdict(int)  #defaultdic를 사용해 비교를 없애고 존재하지 않는 키에 대해 디폴트 리턴
        count=0

        for char in S:
            freqs[char]+=1

        for char in J:
            count += freqs[char]
        return count
w=Solution()
print(w.numJewelsInStones(J="aA",S="aAAbbbb"))