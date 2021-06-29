def solution(progresses, speeds):
    # answer = []
    # time=0 #지나간 날짜를 의미
    # count=0
    # while len(progresses)>0:
    #     if progresses[0]+time*speeds[0]>=100: #지나간 날짜*속도가 100%가 넘을때
    #         progresses.pop(0)
    #         speeds.pop(0)
    #         count+=1 #완성 개수 더함
    #     else:
    #         if(count>0):#이미 완성된게 있을 때
    #             answer.append(count)
    #             count=0 #완성개수 초기화
    #         time+=1
    # answer.append(count) #마지막 개수
    #
    #
    # return answer

###########################################남은 날짜 비교###########################
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:###Q에 입력된 마지막 날짜보다 작으면
            Q[-1][1] += 1
    return [q[1] for q in Q]
print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
