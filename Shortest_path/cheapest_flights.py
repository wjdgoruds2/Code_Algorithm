from typing import List
import heapq
import collections
class Solution:
    def findCheapestPrice(self,n:int, edges:List[List[int]],src:int,dst:int,K:int) -> int:
        graph=collections.defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))

        Q = [(0,src,K)]  #(가격,정점,남은 가능 경유지 수)

        while Q:
            price,node,K=heapq.heappop(Q)
            if node ==dst:
                return price
            if K>=0:
                for v,w in graph[node]:
                    alt=price+w
                    heapq.heappush(Q,(alt,v,K-1))

        return -1




w=Solution()
print(w.findCheapestPrice(n=3,edges=[[0,1,100],[1,2,100],[0,2,500]],src=0,dst=2,K=0))
