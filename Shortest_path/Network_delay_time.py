from typing import List
import heapq
import collections
class Solution:
    def networkDelayTime(self, times:List[List[int]],N:int,K:int) -> int:
        graph=collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w)) #연결을 나타냄

        Q=[(0,K)]   #Q=(쇼요시간,정점)
        dist=collections.defaultdict(int)  #dist=총 각 노드에 소요되는 시간을 저장
        while Q:
            time,node=heapq.heappop(Q)
            if node not in dist:
                dist[node]=time
                for v,w in graph[node]:
                    alt=time+w
                    heapq.heappush(Q,(alt,v)) #####우선순위 큐 :부모노드 > 자식노드 인경우 자식 노드 중 작은 노드와 변경 ex) 5 2 1 -> 5 2 -> 2 5 -> 2 5 1-> 1 5 2

        if len(dist) == N :
            return max(dist.values())
        return -1



w=Solution()
print(w.networkDelayTime(times=[[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]],N=8,K=3))
