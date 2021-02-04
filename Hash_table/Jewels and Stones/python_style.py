class Solution:
    def numJewelsInStones(self,J:str,S:str)->int:
        return sum(s in J for s in S) #s in J:J에 있는 문자가 for s in S =S에 있는 문자가 있는지 여부 True,False
w=Solution()
print(w.numJewelsInStones(J="aA",S="aAAbbbb"))