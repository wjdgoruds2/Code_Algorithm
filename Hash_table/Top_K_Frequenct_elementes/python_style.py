import collections

class Solution:
    def topKFrequent(self,num,k):
        return list(zip(*collections.Counter(num).most_common(k)))[0]   ###zip으로 묶으면 [((1,2),), ((2,2),)] 그래서 *로 언패킹해줘야함
        # Ex) for f in fruits:
        #     print(f,end=' ')
        #
        #     But!!!
        #
        #     =print(*fruits)
w=Solution()
print(w.topKFrequent(num=[1,1,1,2,2,3],k=2))
