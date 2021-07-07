def solution(arr, divisor):
    #한줄 표현 가능
    return sorted(s for s in arr if s>=divisor and s%divisor==0) or [-1]
    # answer = []
    # answer+=(sorted(s for s in arr if s>=divisor and s%divisor==0))
    # if len(answer)==0:
    #     return [-1]
    # return answer
print(solution([5, 9, 7, 10],5))
print(solution([2, 36, 1, 3],1))
print(solution([3,2,6],10))
