# from collections import deque
# def solution(priorities, location):
#     answer=0
#     dep=deque(priorities)
#     depnum=[i+1 for i in range(len(priorities))] ###값들위치
#     orderdep=deque(depnum)
#     while len(dep)>0:
#         pre=dep.popleft()
#         prenum=orderdep.popleft()
#         if (len(dep)>0 and max(dep)>pre):
#             dep.append(pre)
#             orderdep.append(prenum)
#         else:
#             answer += 1  ########다 정렬되고 해당 값의 위치를 계산
#             if (prenum == location+1): #deque의 젤 앞값이 원하는 값이 나올때 까지 반복
#                 return answer
#     return answer

2
3
4
5
6
7
8
9
10
11
12
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): ##########이중 하나로 있으면! any사용
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))