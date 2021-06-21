from typing import List
import collections
class Solution:
    def findItinerary(self,tickets:List[List[str]])->List[str]:
        graph=collections.defaultdict(list)
        for a,b in sorted(tickets):
            graph[a].append(b)

        route,stack=[],['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]

w=Solution()
print(w.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
