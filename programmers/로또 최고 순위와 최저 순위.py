def solution(lottos, win_nums):
    answer = [0,0]
    cnt=0
    num=0
    rank=[6,6,5,4,3,2,1]
    for i in win_nums:
        if i in lottos:
            cnt+=1
    # for j in lottos:
    #     if j ==0:
    #         num+=1
    num=lottos.count(0) #0의 개수
    answer[0],answer[1]=rank[cnt+num],rank[cnt]
    return answer
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
