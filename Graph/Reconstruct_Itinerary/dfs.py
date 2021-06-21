from typing import List
import collections
class Solution:
    def findItinerary(self,tickets:List[List[str]])->List[str]:
        graph=collections.defaultdict(list)
        for a,b in sorted(tickets):
            graph[a].append(b)

        route=[]
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0)) ####알파벳 빠른순
            route.append(a)

        dfs('JFK')
        return route[::-1]

w=Solution()
print(w.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
