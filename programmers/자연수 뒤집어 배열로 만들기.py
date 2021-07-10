def solution(n):
    # new_n=[int(i) for i in str(n)]
    # answer=[]
    # for num in range(len(new_n)):
    #     answer.append(new_n.pop())
    # return answer
    return list(map(int,reversed(str(n))))
print(solution(12345))