def solution(left, right):
    # answer = 0
    # num=[]
    # for i in range(left,right+1):
    #     for j in range(1,i+1):
    #         if i%j==0:
    #             num.append(j)
    #     print(num)
    #     if len(num)%2==0:
    #         answer+=i
    #         num = []
    #     else:
    #         answer -= j
    #         num = []
    # return answer


######################제곱으로 풀기
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:  #################제곱수만 (ex>14,25,36...) 약수의 개수가 홀수다!!!!!!!!!!!
            answer-=i
        else:
            answer+=i
    return answer


print(solution(13,17))