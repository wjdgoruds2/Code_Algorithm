def solution(absolutes, signs):
    answer = 0
    for i,num in enumerate(absolutes):
        if signs[i]:
            answer+= num
        else:
            answer-= num
    return answer
print(solution([4, 7, 12], [true, false, true]))