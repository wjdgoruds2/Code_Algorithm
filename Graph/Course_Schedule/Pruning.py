from typing import List
import collections
class Solution:
    def canFinsh(self,numCourse:int,prerequisites:List[List[int]])->bool:
        graph=collections.defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)

        traced=set()
        visited=set()
        def dfs(i):
            if i in traced:
                return False
            if i in visited:   #####이미 방문노드 다시 방문 x
                return True
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)  ######탐색종료 후 순환 노드 삭제
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
w=Solution()
print(w.canFinsh(numCourse=2,prerequisites=[[0,1],[0,2],[1,2]]))
