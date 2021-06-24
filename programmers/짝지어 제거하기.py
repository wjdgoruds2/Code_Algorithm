def solution(s):
    new_s=[]
    for i in s:
        if len(new_s)==0:
            new_s.append(i)
        else:
            if i==new_s[-1]:
                new_s.pop()
            else:
                new_s.append(i)
    if len(new_s)==0:
        answer = 1
    else:
        answer=0
    return answer

##########answer자체를 list화해서 not(answer)=1
    # answer = []
    # for i in s:
    #     if not (answer):
    #         answer.append(i)
    #     else:
    #         if (answer[-1] == i):
    #             answer.pop()
    #         else:
    #             answer.append(i)
    # return not (answer)

print(solution('baabaa'))
print(solution('cdcd'))