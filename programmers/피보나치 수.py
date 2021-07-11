def solution(n):
    ################################재귀는 시간 초과####################
    # if n==0:
    #     return 0
    # elif n==1 or n==2:
    #     return 1
    # else:
    #     return (solution(n-1)+solution(n-2))%1234567
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
print(solution(3))
print(solution(5))