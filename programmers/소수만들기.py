from itertools import combinations
def isprime(num): #######소수인지 검사
    if num==0 or num==1: #더한값이 1과 0일리는 없음
        return False
    else:
        for j in range(2,num): #나누어 떨어지면 소수 아님
            if num % j == 0:
                return False
        return True

def solution(nums):
    answer = 0
    combine= list(combinations(nums,3)) #반복숫자 없이 3개씩 조합 list화
    print(combine)
    for i in combine:
        if isprime(sum(i)):
            answer+=1 #소수면 답 증가

    return answer
print(solution([1,2,3,4]))