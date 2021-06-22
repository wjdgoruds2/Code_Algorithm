def solution(a, b):
    answer = 0
    for i in range(0,len(a)):
        answer += a[i]*b[i]

        #zip():두 그룹의 데이터를 서로 엮어주는 파이썬의 내장 함수
        #return sum([x*y for x, y in zip(a,b)])
    return answer
print(solution([1,2,3,4],[-3,-1,0,2]))