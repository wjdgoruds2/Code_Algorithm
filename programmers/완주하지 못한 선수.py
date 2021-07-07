def solution(participant, completion):


#######내가 처음에 생각한 dic key,value이용 =>정확성은 만점이나 효율성은 0점
    # answer = ''
    # for i,name in enumerate(completion):
    #     participant.remove(name)
    # answer=participant
    # return answer

#######dic[이름]=1로
    temp={}
    for i in participant:
        temp[i]+=temp.get(i,0)+1 ######한줄로 아래를 해결 가능
        # if i in temp:
        #     temp[i]+=1 #동명이인
        # else:
        #     temp[i]=1 #일반 참여인
    for j in completion:
        if temp[j]==1:#이름 같으면 temp[이름]삭제
            del temp[j] 
        else: 
            temp[j]-=1 #####동명이인이면 1감소
    return list(temp.keys())[0]


#######hask사용
    # answer = ''
    # temp = 0
    # dic = {}
    # for part in participant:
    #     dic[hash(part)] = part
    #     temp += int(hash(part))
    # for com in completion:
    #     temp -= hash(com)
    # answer = dic[temp]
    #
    # return answer

#############collections.Counter사용->Counter=값+개수 dic형태로 출력
    # import collections
    #
    #
    # def solution(participant, completion):
    #     answer = collections.Counter(participant) - collections.Counter(completion)
    #     return list(answer.keys())[0]

##############zip(p,c)-> (p),(c)비교 가능
    # def solution(participant, completion):
    #     participant.sort()
    #     completion.sort()
    #     for p, c in zip(participant, completion):
    #         if p != c:
    #             return p
    #     return participant[-1]
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
